from django.db import models
from businessrules.models import BusinessRule
from states_simplicity.models import State
from types_simplicity.models import Type


class Requirement(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512, blank=False)
    description = models.TextField(blank=True)
    type_id = models.ForeignKey(Type)
    state_id = models.ForeignKey(State)
    date_created = models.DateTimeField(blank=False)
    date_modified = models.DateTimeField(blank=False)
    code = models.CharField(max_length=45, blank=False)
    business_type = models.CharField(max_length=255, blank=False)
    keywords = models.TextField(blank=True)
    is_active = models.CharField(max_length=20, blank=False)

    def __unicode__(self):
        return self.title


class RequirementBusinessRule(models.Model):
    requirement_business_rule_id = models.AutoField(primary_key=True)
    requirement_id = models.ForeignKey(Requirement)
    business_rule_id = models.ForeignKey(BusinessRule)

    def __unicode__(self):
        return self.requirement_business_rule_id

    class Meta:
        unique_together = (("requirement_id", "business_rule_id"),)


class RequirementInput(models.Model):
    requirement_input_id = models.AutoField(primary_key=True)
    requirement_id = models.ForeignKey(Requirement)
    value = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.requirement_input_id


class RequirementOutput(models.Model):
    requirement_output_id = models.AutoField(primary_key=True)
    requirement_id = models.ForeignKey(Requirement)
    value = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.requirement_output_id


class AcceptanceCriteria(models.Model):
    acceptance_criteria_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    requirement_id = models.ForeignKey(Requirement)
    date_created = models.DateTimeField(blank=False)
    date_modified = models.DateTimeField(blank=False)
    code = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.name
