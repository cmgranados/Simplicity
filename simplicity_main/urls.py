from django.conf.urls import patterns, include, url

from django.contrib import admin
from kappa.requirements.views import RequirementListView
from rest_framework.routers import DefaultRouter
from kappa.businessrules.views import BusinessRuleView
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView


sqs = SearchQuerySet().facet('text')
admin.autodiscover()

router = DefaultRouter()
router.register(r'businessrules', BusinessRuleView)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^kappa/requirements/$', RequirementListView.as_view(), name='requirement-list'),
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^kappa/requirements/search/', FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs, template="requirements/search/search.html"), name='haystack_search',),
)
