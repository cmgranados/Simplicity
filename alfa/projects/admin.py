from django.contrib import admin

from .models import Project, ProjectAssociation, RequirementAssociation

admin.site.register(Project)
admin.site.register(ProjectAssociation)
admin.site.register(RequirementAssociation)
