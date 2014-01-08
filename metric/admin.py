from django.contrib import admin
#from metric.models import Environment, Metric, UseCase, Sample
from metric.models import Metric, Sample

#admin.site.register(Environment)
admin.site.register(Metric)
#admin.site.register(UseCase)
admin.site.register(Sample)


# vim: set et sw=4 ts=4:
