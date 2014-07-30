from django.db import models
from shared.types_simplicity.models import Type
from shared.states_simplicity.models import State
from kappa.businessrules.models import BusinessRule


class Requirement(models.Model):
    requirement = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512, blank=False)
    description = models.TextField(blank=True)
    type = models.ForeignKey(Type)
    state = models.ForeignKey(State)
    date_created = models.DateTimeField(blank=False)
    date_modified = models.DateTimeField(blank=False)
    code = models.CharField(max_length=45, blank=False)
    business_type = models.CharField(max_length=255, blank=False)
    keywords = models.TextField(blank=True)
    is_active = models.CharField(max_length=20, blank=False)

    def __unicode__(self):
        return self.title
    class Meta:
        db_table = "req_requirement"


class RequirementBusinessRule(models.Model):
    requirement_business_rule = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    business_rule = models.ForeignKey(BusinessRule)

    def __unicode__(self):
        return self.requirement_business_rule

    class Meta:
        unique_together = (("requirement", "business_rule"),)
        db_table = "req_requirement_business_rule"


class RequirementInput(models.Model):
    requirement_input = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    value = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.requirement_input
    class Meta:
        db_table = "req_requirement_input"


class RequirementOutput(models.Model):
    requirement_output = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    value = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.requirement_output
    class Meta:
        db_table = "req_requirement_output"


class AcceptanceCriteria(models.Model):
    acceptance_criteria = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    requirement = models.ForeignKey(Requirement)
    date_created = models.DateTimeField(blank=False)
    date_modified = models.DateTimeField(blank=False)
    code = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "req_acceptance_criteria"
