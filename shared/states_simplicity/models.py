from django.db import models


class StateType(models.Model):
    state_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=True)
    state_type_id = models.ForeignKey(StateType)

    def __unicode__(self):
        return self.name
