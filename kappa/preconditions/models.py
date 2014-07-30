from django.db import models
from kappa.requirements.models import Requirement


class Precondition(models.Model):
    precondition_id = models.AutoField(primary_key=True)
    requirement_id = models.ForeignKey(Requirement)

    def __unicode__(self):
        return self.precondition_id


class PreconditionRequirement(models.Model):
    precondition_requirement_id = models.AutoField(primary_key=True)
    requirement_id = models.ForeignKey(Requirement)
    precondition_id = models.ForeignKey(Precondition)

    def __unicode__(self):
        return self.precondition_id

    class Meta:
        unique_together = (("requirement_id", "precondition_id"),)


class PreconditionDescription(models.Model):
    precondition_description_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)
    precondition_id = models.ForeignKey(Precondition)

    def __unicode__(self):
        return self.precondition_id
