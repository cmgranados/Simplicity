from django.contrib import admin


from .models import TypeClassification, Type, TypeParentType

admin.site.register(TypeClassification)
admin.site.register(Type)
admin.site.register(TypeParentType)
