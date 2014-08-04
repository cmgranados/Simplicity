from django.contrib import admin


from .models import Requirement, RequirementBusinessRule, RequirementInput

admin.site.register(Requirement)
admin.site.register(RequirementBusinessRule)
admin.site.register(RequirementInput)
