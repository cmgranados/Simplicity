from django.contrib import admin

from omicron.testcases.models import TestCase, TestCaseInput, \
    TestCaseRequirement, TestCaseProcedure, TestCaseUpdateAuthor


# Register your models here.
admin.site.register(TestCase)
admin.site.register(TestCaseInput)
admin.site.register(TestCaseRequirement)
admin.site.register(TestCaseProcedure)
admin.site.register(TestCaseUpdateAuthor)
