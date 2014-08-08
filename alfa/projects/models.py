from django.db import models
from shared.types_simplicity.models import Type
from shared.states_simplicity.models import State
from django.contrib.auth.models import User 
from kappa.requirements.models import Requirement

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    type = models.ForeignKey(Type, related_name='project_projecttype')
    business_type = models.ForeignKey(Type, related_name='project_businesstype')
    client_type = models.ForeignKey(Type, related_name='project_clienttype')
    date_started = models.DateTimeField(blank=False)
    date_created = models.DateTimeField(blank=False)
    date_modified = models.DateTimeField(blank=False)
    description = models.TextField(null=True)
    partaker = models.ForeignKey(User)
    keywords=models.CharField(max_length=512, null=True)
    
    
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "af_pr_project"
        
class ProjectAssociation(models.Model):
    association_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, related_name='projectassociation_projectid')
    association_project = models.ForeignKey(Project, related_name='projectassociation_associationproject')

    def __unicode__(self):
        return self.association_id

    class Meta:
        unique_together = (("project_id", "association_project"),)
        db_table = "af_pj_project_association"

class RequirementAssociation(models.Model):
    association_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project)
    requirement_id = models.ForeignKey(Requirement)

    def __unicode__(self):
        return self.association_id

    class Meta:
        unique_together = (("project_id", "requirement_id"),)
        db_table = "af_pj_requirement_association"

# Create your models here.
