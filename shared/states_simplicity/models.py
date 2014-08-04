from django.db import models


class StateType(models.Model):
    state_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "adm_state_type"


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=True, null=True)
    state_type = models.ForeignKey(StateType)

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "adm_state"
