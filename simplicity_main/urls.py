from django.conf.urls import patterns, include, url

from django.contrib import admin
from kappa.requirements.views import RequirementListView
from rest_framework.routers import DefaultRouter
from kappa.businessrules.views import BusinessRuleView
admin.autodiscover()

router = DefaultRouter()
router.register(r'businessrules', BusinessRuleView)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^kappa/requirements/$', RequirementListView.as_view(), name='requirement-list'),
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
