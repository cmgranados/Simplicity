from django.contrib import admin


from .models import Requirement, RequirementBusinessRule, RequirementInput

admin.site.register(Requirement, RequirementBusinessRule, RequirementInput)
