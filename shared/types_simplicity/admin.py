from django.contrib import admin


from .models import TypeClassification, Type

admin.site.register(TypeClassification, Type)
