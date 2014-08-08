from django.db import models
from shared.types_simplicity.models import Type
from shared.states_simplicity.models import State

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "af_pr_project"

# Create your models here.
