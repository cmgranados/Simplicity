from django.db import models
from shared.types_simplicity.models import Type
from shared.states_simplicity.models import State
from kappa.businessrules.models import BusinessRule
from django.contrib.auth.models import User


class Requirement(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512, blank=False)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(Type)
    state = models.ForeignKey(State)
    date_created = models.DateTimeField(blank=False)
    date_modified = models.DateTimeField(blank=False)
    code = models.CharField(max_length=45, blank=False)
    keywords = models.CharField(max_length=512, null=True)
    is_active = models.CharField(max_length=20, blank=False)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "kp_req_requirement"


class RequirementBusinessRule(models.Model):
    requirement_business_rule_id = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    business_rule = models.ForeignKey(BusinessRule)

    def __unicode__(self):
        return str(self.requirement_business_rule_id)

    class Meta:
        unique_together = (("requirement", "business_rule"))
        db_table = "kp_req_requirement_business_rule"


class RequirementInput(models.Model):
    requirement_input_id = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    input = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True)
    data_type = models.ForeignKey(Type)

    def __unicode__(self):
        return str(self.requirement_input_id)

    class Meta:
        db_table = "kp_req_requirement_input"


class RequirementOutput(models.Model):
    requirement_output_id = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    output = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True)
    data_type = models.ForeignKey(Type)

    def __unicode__(self):
        return str(self.requirement_output_id)

    class Meta:
        db_table = "kp_req_requirement_output"


class AcceptanceCriteria(models.Model):
    acceptance_criteria_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    requirement = models.ForeignKey(Requirement)
    date_created = models.DateTimeField(blank=False)
    date_modified = models.DateTimeField(blank=False)
    code = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "kp_req_acceptance_criteria"

class RequirementUpdateAuthor(models.Model):
    requirement_update_author_id = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    author = models.ForeignKey(User)
    update_date = models.DateTimeField(blank=False)
    
    def __unicode__(self):
        return str(self.requirement_author_id)

    class Meta:
        db_table = "kp_req_requirement_update_author"
