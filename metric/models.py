from django.db import models


class Metric(models.Model):
    class Meta:
        db_table = 'metric'

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=128)
    explanation_url = models.CharField(max_length=256)
    units = models.CharField(max_length=128)


class Environment(models.Model):
    class Meta:
        db_table = 'environment'


class Procedure(models.Model):
    class Meta:
        db_table = 'procedure'


class Sample(models.Model):
    class Meta:
        db_table = 'samples'
        ordering = ['metric', 'sample_date']
        unique_together = ('metric', 'sample_date')

    def __unicode__(self):
        return '{0}/{1}: {2}'.format(self.sample_date, self.metric.name, self.value)

    metric = models.ForeignKey(Metric)
    sample_date = models.DateField()
    value = models.FloatField()
    environment = models.ForeignKey(Environment, blank=True, null=True)
    procedure = models.ForeignKey(Procedure, blank=True, null=True)


# vim: set et sw=4 ts=4:
