from django.db import models
from shared.types_simplicity.models import Type
from shared.states_simplicity.models import State


class BusinessRule(models.Model):
    business_rule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True)
    type = models.ForeignKey(Type)
    state_type = models.ForeignKey(State)
    date_created = models.DateTimeField(blank=False)
    date_modified = models.DateTimeField(blank=False)
    code = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "br_business_rule"
