from django.contrib import admin

from kappa.requirements.models import RequirementOutput

from .models import Requirement, RequirementBusinessRule, RequirementInput


admin.site.register(Requirement)
admin.site.register(RequirementBusinessRule)
admin.site.register(RequirementInput)
admin.site.register(RequirementOutput)
