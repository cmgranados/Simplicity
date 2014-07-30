from django.db import models
from kappa.requirements.models import Requirement


class Precondition(models.Model):
    precondition = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)

    def __unicode__(self):
        return self.precondition
    class Meta:
        db_table = "pco_pre_condition"


class PreconditionRequirement(models.Model):
    precondition_requirement = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    precondition = models.ForeignKey(Precondition)

    def __unicode__(self):
        return self.precondition

    class Meta:
        unique_together = (("requirement", "precondition"),)
        db_table = "pco_pre_condition_requirement"


class PreconditionDescription(models.Model):
    precondition_description = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)
    precondition = models.ForeignKey(Precondition)

    def __unicode__(self):
        return self.precondition
    class Meta:
        db_table = "pco_pre_condition_description"
