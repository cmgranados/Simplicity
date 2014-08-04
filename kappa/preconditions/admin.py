from django.contrib import admin

from .models import Precondition, PreconditionRequirement, PreconditionDescription

admin.site.register(Precondition, PreconditionRequirement, PreconditionDescription)
