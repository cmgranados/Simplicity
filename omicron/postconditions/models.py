from django.db import models
from omicron.testcases.models import TestCase


class Postcondition(models.Model):
    postcondition_id = models.AutoField(primary_key=True)
    test_case = models.ForeignKey(TestCase)

    def __unicode__(self):
        return str(self.postcondition_id)
    
    class Meta:
        db_table = "om_pos_postcondition"


class PostconditionTestCase(models.Model):
    postcondition_test_case_id = models.AutoField(primary_key=True)
    test_case = models.ForeignKey(TestCase)
    postcondition = models.ForeignKey(Postcondition)

    def __unicode__(self):
        return str(self.postcondition_test_case_id)

    class Meta:
        unique_together = (("test_case", "postcondition"),)
        db_table = "om_pos_postcondition_test_case"


class PostconditionDescription(models.Model):
    postcondition_description_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    postcondition = models.ForeignKey(Postcondition)

    def __unicode__(self):
        return str(self.postcondition_description_id)
        
    class Meta:
        db_table = "om_pos_postcondition_description"
