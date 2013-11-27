from datetime import datetime, timedelta
from django.http import HttpResponse
from django.template import RequestContext, loader
import json
#import logging

from models import Sample

#log = logging.getLogger('django.db.backends')
#log.setLevel(logging.DEBUG)
#log.addHandler(logging.StreamHandler())


def index(request):
    template = loader.get_template('metric/index.html')

    metrics = []
    now = datetime.now()
    for sample in Sample.objects.filter(sample_date__range=(now -
                                        timedelta(days=90),
                                        now)).select_related():
        name = sample.metric.name
        metric = filter(lambda m: m['name'] == name, metrics)
        if len(metric):
            metric = metric[0]
        else:
            metric = {'name': name, 'samples': [],
                      'units': sample.metric.units, 'url': sample.metric.explanation_url}
            metrics.append(metric)

        metric['samples'].append({'date': sample.sample_date.strftime('%Y-%m-%dT%H:%M:%S'),
                                  'value': sample.value})

    context = RequestContext(request, {
        'metrics': json.dumps(metrics)
    })

    return HttpResponse(template.render(context))


# vim: set et sw=4 ts=4:
