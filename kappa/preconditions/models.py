from django.db import models
from kappa.requirements.models import Requirement


class Precondition(models.Model):
    precondition_id = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)

    def __unicode__(self):
        return str(self.precondition_id)
    
    class Meta:
        db_table = "kp_pco_precondition"


class PreconditionRequirement(models.Model):
    precondition_requirement_id = models.AutoField(primary_key=True)
    requirement = models.ForeignKey(Requirement)
    precondition = models.ForeignKey(Precondition)

    def __unicode__(self):
        return str(self.precondition_requirement_id)

    class Meta:
        unique_together = (("requirement", "precondition"),)
        db_table = "kp_pco_precondition_requirement"


class PreconditionDescription(models.Model):
    precondition_description_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    precondition = models.ForeignKey(Precondition)

    def __unicode__(self):
        return str(self.precondition_description_id)
    class Meta:
        db_table = "kp_pco_precondition_description"
