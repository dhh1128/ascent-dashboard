from django.contrib import admin
#from metric.models import Environment, Metric, Procedure, Sample
from metric.models import Metric, Sample

#admin.site.register(Environment)
admin.site.register(Metric)
#admin.site.register(Procedure)
admin.site.register(Sample)


# vim: set et sw=4 ts=4:
