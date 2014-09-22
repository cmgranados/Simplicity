from django.db import models
from kappa.requirements.models import Requirement
from shared.states_simplicity.models import State
from shared.types_simplicity.models import Type
from django.contrib.auth.models import User


class TestCase(models.Model):	
    test_case_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, blank=False)
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
        return self.name
    
    class Meta:
        db_table = "om_tc_test_case"


class TestCaseInput(models.Model):
    test_case_input_id = models.AutoField(primary_key=True)
    test_case_id = models.ForeignKey(TestCase)
    input = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True)
    data_type = models.ForeignKey(Type)

    def __unicode__(self):
        return str(self.test_case_input_id)

    class Meta:
        db_table = "om_tc_test_case_input"


class TestCaseRequirement(models.Model):
    test_case_requirement_id = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    test_case = models.ForeignKey(TestCase)

    def __unicode__(self):
        return str(self.test_case_requirement_id)

    class Meta:
        db_table = "om_tc_test_case_requirement"


class TestCaseProcedure(models.Model):
    test_case_procedure_id = models.AutoField(primary_key=True)
    step = models.CharField(max_length=50, blank=True)
    activity = models.TextField(blank=True, null=True)
    test_case = models.ForeignKey(TestCase)

    def __unicode__(self):
        return str(self.test_case_procedure_id)

    class Meta:
        db_table = "om_tc_test_case_procedure"
