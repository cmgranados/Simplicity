from django.contrib import admin


from .models import StateType, State

admin.site.register(StateType, State)
