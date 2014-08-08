from django.db import models
from shared.types_simplicity.models import Type
from shared.states_simplicity.models import State
from django.contrib.auth.models import User 
from kappa.requirements.models import Requirement

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    type = models.ForeignKey(Type)
    business_type = models.ForeignKey(Type)
    client_type = models.ForeignKey(Type)
    projec_type = models.ForeignKey(Type)
    state_type = models.ForeignKey(State)
    date_started = models.DateTimeField(blank=False)
    date_created = models.DateTimeField(blank=False)
    date_modified = models.DateTimeField(blank=False)
    description = models.TextField(blank=True, null=True)
    partaker = models.ForeignKey(User)
    keywords=models.CharField(max_length=512, null=True)
    
    
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "af_pr_project"
        
class Project_association(models.Model):
    association_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project)
    association_project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.association_id

    class Meta:
        unique_together = (("project_id", "association_project"),)
        db_table = "af_pj_project_association"

class Requirement_association(models.Model):
    association_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project)
    requirement_id = models.ForeignKey(Requirement)

    def __unicode__(self):
        return self.association_id

    class Meta:
        unique_together = (("project_id", "requirement_id"),)
        db_table = "af_req_requirement_association"

# Create your models here.
