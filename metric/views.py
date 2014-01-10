from datetime import datetime, timedelta
from django.http import HttpResponse
from django.template import RequestContext, loader
import json
#import logging

from models import Sample
from models import UseCase

#log = logging.getLogger('django.db.backends')
#log.setLevel(logging.DEBUG)
#log.addHandler(logging.StreamHandler())

def index(request):
    template = loader.get_template('metric/index.html')

    usecases = []
    now = datetime.now()
    #for sample in Sample.objects.filter(sample_date__range=(now -
    #                                    timedelta(days=90),
    #                                    now)).filter(use_case_id__exact=1).select_related():
    for usecase in UseCase.objects.all():
        metrics = []
        metricName = ""
        for sample in Sample.objects.filter(sample_date__range=(now -
                                            timedelta(days=90),
                                            now)).filter(use_case_id__exact=usecase.id).select_related():
            metricName = sample.metric.name
            metric = filter(lambda m: m['name'] == metricName, metrics)
            if len(metric):
                metric = metric[0]
            else:
                metric = {'name': metricName,
                          'samples': [],
                          'units': sample.metric.units, 'url': sample.metric.explanation_url}
                metrics.append(metric)

            metric['samples'].append({'date': sample.sample_date.strftime('%Y-%m-%dT%H:%M:%S'),
                                      'value': sample.value})

        usecases.append({ 'id': usecase.id, 'name' :usecase.name, 'metrics': metrics })

    context = RequestContext(request, {
        'usecases': json.dumps(usecases)
    })

    return HttpResponse(template.render(context))


# vim: set et sw=4 ts=4:
