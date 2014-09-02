import debug_toolbar
from django.conf.urls import patterns, include, url
from django.contrib import admin
from haystack.query import SearchQuerySet
from rest_framework.routers import DefaultRouter
from kappa.businessrules.views import BusinessRuleView
from kappa.requirements.forms import RequirementSearchForm
from kappa.requirements.views import FacetedSearchView
from simplicity_main.views import logout


sqs = SearchQuerySet().facet('text')
admin.autodiscover()

router = DefaultRouter()
router.register(r'businessrules', BusinessRuleView)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^kappa/requirements/$', RequirementListView.as_view(), name='requirement-list'),
                       url(r'^$', 'simplicity_main.views.index'),
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^signup/', 'shared.userprofiles.views.signup', name='signup'),
                       url(r'^signin/', 'shared.userprofiles.views.signin', name='signin'),
                       url('', include('social.apps.django_app.urls', namespace='social')),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
                       url(r'^logout_auth/$', logout, name='logout_auth'),
                       url(r'^kappa/requirements/$', FacetedSearchView(form_class=RequirementSearchForm, searchqueryset=sqs, template="requirements/search.html"), name='haystack_search',),
                       # wizard ejemplo
                       url(r'^__debug__/', include(debug_toolbar.urls)),
                       url(r'^search/$', 'kappa.requirements.views.searchRequirements'),
                       url(r'^kappa/businessrules_ajax_search/$', 'kappa.requirements.views.searchBusinessRules'),
                       url(r'^kappa/preconditions_ajax_search/$', 'kappa.requirements.views.searchRequirements'),
                       url(r'^kappa/requirements/new_requirement', 'kappa.requirements.views.new_requirement', name='new_requirement'),
                       url(r'^kappa/$', 'kappa.views.kappa_home'),
                       url(r'^save_requirement_definition/$', 'kappa.requirements.views.save_requirement_definition'),
                       url(r'^kappa/requirements/delete_requirement_ajax', 'kappa.requirements.views.delete_requirement'),
)
