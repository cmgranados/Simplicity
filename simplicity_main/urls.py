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
                       url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^kappa/requirements/$', RequirementListView.as_view(), name='requirement-list'),
                       url(r'^$', 'simplicity_main.views.index'),
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^signup/', 'shared.userprofiles.views.signup', name='signup'),
                       url('', include('social.apps.django_app.urls', namespace='social')),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
                       url(r'^logout_auth/$', logout, name='logout_auth'),
                       # wizard ejemplo
                       url(r'^__debug__/', include(debug_toolbar.urls)),
                       url(r'^search/$', 'kappa.requirements.views.searchRequirements'),
                       url(r'^kappa/$', 'kappa.views.kappa_home'),
                       url(r'^kappa/businessrules_ajax_search/$', 'kappa.requirements.views.searchBusinessRules'),
                       url(r'^kappa/requirements_ajax_search/$', 'kappa.requirements.views.searchRequirements'),
                       url(r'^kappa/requirements/$', FacetedSearchView(form_class=RequirementSearchForm, searchqueryset=sqs, template="requirements/search.html"), name='haystack_search',),
                       url(r'^kappa/requirements/new_requirement', 'kappa.requirements.views.new_requirement', name='new_requirement'),
                       url(r'^kappa/requirements/delete_requirement_ajax', 'kappa.requirements.views.delete_requirement'),
                       url(r'^alfa/projects$', 'alfa.projects.views.home_projects', name="projects"),
                       url(r'^alfa/projects/search$', 'alfa.projects.views.search_projects', name="projectsSearch"),
                       url(r'^alfa/sync/$', 'alfa.projects.views.sync', name='sync'),
                       url(r'^kappa/save_requirement_ajax/$', 'kappa.requirements.views.save_requirement_ajax'),
                       url(r'^kappa/new_businessrule_ajax/$', 'kappa.businessrules.views.new_businessrule_ajax'),
                       url(r'^kappa/requirements/update_requirement', 'kappa.requirements.views.update_requirement'),
                       url(r'^omicron/testcases/new', 'omicron.testcases.views.new_test_case', name='new_test_case'),
                       url(r'^kappa/get_businessrules_types_ajax/$', 'kappa.businessrules.views.get_businessrules_types_ajax'),
                       url(r'^types/get_data_types_ajax/$', 'shared.types_simplicity.views.get_data_types_ajax'),
					   url(r'^omicron/$', 'omicron.views.omicron_home'),
                       url(r'^omicron/testcases$', 'omicron.testcases.views.home_test_cases', name="testcases"),
                       url(r'^omicron/testcases/search$', 'omicron.testcases.views.search_test_cases', name="testcases_search"),
                       url(r'^omicron/save_testcase_ajax/$', 'omicron.testcases.views.save_testcase_ajax'),
                       url(r'^omicron/testcases/update-testcase', 'omicron.testcases.views.update_testcase'),
)
