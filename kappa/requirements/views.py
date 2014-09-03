import logging

from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic.list import ListView
from haystack.query import SearchQuerySet
from haystack.views import SearchView

from kappa.requirements.forms import RequirementForm1, RequirementForm2, RequirementForm3, RequirementForm4, RequirementForm5
from kappa.requirements.models import Requirement
from kappa.businessrules.models import BusinessRule
from jira.client import JIRA

# Get an instance of a logger
logger = logging.getLogger('simplicity_main.kappa.requirements.views')

# Create your views here.
class RequirementListView(ListView):
    model = Requirement

    def get_context_data(self, **kwargs):
        context = super(RequirementListView, self).get_context_data(**kwargs)
        return context


class FacetedSearchView(SearchView):

    def extra_context(self):
        extra = super(FacetedSearchView, self).extra_context()

        if self.results == []:
            extra['facets'] = self.form.search().facet_counts()
        else:
            extra['facets'] = self.results.facet_counts()

        return extra


def searchRequirements(request):
    if not request.POST.get('q', '') :
        content_auto_v = "descripcion"
    else:
        content_auto_v=request.POST.get('q', '')
        
    requirements = SearchQuerySet().models(Requirement).filter(text=content_auto_v)
    return render_to_response('ajax_search.html', {'requirements': requirements})


def searchBusinessRules(request):
    if not request.POST.get('br', '') :
        content_auto_v = ""
    else:
        content_auto_v=request.POST.get('br', '')
         
    businessrules = SearchQuerySet().models(BusinessRule).filter(text=content_auto_v)
    return render_to_response('ajax_businessrule_search.html', {'businessrules': businessrules})


def new_requirement(request):
    return render(request, 'requirement_form_base.html')

def save_requirement_definition(request):
    return render_to_response('done.html')

def search_jira_projects(request):
    key_cert_data = None
    with open('C:\dev\jira.pem', 'r') as key_cert_file:
        key_cert_data = key_cert_file.read()
    logger.debug('key_cert_data' + key_cert_data)
    oauth_dict = {
        'access_token': 'srkLiVajV2EtYhHhgi2x8DJjpoqSyXaN',
        'access_token_secret': 'qkjFBvRxAwAZb4ygpTObr1IhJfPmy0h1',
        'consumer_key': 'simplicity',
        'key_cert': key_cert_data
    }
    options = {
        'server': 'https://itcsas.atlassian.net',
    }
    
    jira = JIRA(options=options, oauth=oauth_dict)
    
    # Get all projects viewable by anonymous users.
    projects_main = jira.projects()
    projects = []
    
    for project in projects_main:
        projects.append(jira.project(project.id))
    logger.debug("Cantidad: " + str(projects))
    return render_to_response('jira_projects_list.html', {'projects': projects})
