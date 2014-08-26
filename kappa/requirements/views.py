from datetime import datetime, timedelta
import time

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.views.generic.list import ListView
from haystack.query import SearchQuerySet
from haystack.views import SearchView

from kappa.businessrules.models import BusinessRule
from kappa.requirements.models import Requirement
from shared.states_simplicity.models import State
from shared.types_simplicity.models import Type
from simplicity_main.settings import STATE_REGISTERED, ACTIVE, \
    PRECONDITION_TYPE_REQ_ES


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
        content_auto_v = request.POST.get('q', '')
        
    requirements = SearchQuerySet().models(Requirement).filter(text=content_auto_v)
    return render_to_response('ajax_search.html', {'requirements': requirements})


def searchBusinessRules(request):
    if not request.POST.get('br', '') :
        content_auto_v = ""
    else:
        content_auto_v = request.POST.get('br', '')
         
    businessrules = SearchQuerySet().models(BusinessRule).filter(text=content_auto_v)
    return render_to_response('ajax_businessrule_search.html', {'businessrules': businessrules})


def new_requirement(request):
    return render(request, 'requirement_form_base.html')

def save_requirement_definition(request):
    if request.method == "POST": 
        new_requirement = Requirement()
        
        requirement_title = request.POST.get('requirement_title', None)
        new_requirement.title = requirement_title
        
        requirement_code = request.POST.get('requirement_code', None)
        new_requirement.code = requirement_code
        
        requirement_date_created = datetime.now()
        new_requirement.date_created = requirement_date_created
        
        requirement_type = request.POST.get('requirement_type', None)
        type_retrieved = Type.objects.get(type_id=requirement_type) 
        new_requirement.type = type_retrieved
        
        requirement_description = request.POST.get('requirement_description', None)
        new_requirement.description = requirement_description
        
        state = State.objects.get(state_id=STATE_REGISTERED) 
        new_requirement.state = state
        new_requirement.date_modified = requirement_date_created
        new_requirement.is_active = ACTIVE
        
        requirement_keywords = request.POST.get('requirement_keywords', None)
        new_requirement.keywords = requirement_keywords
        
        new_requirement.save()
        
        # loop through keys
        prerequirement_counter = 0
        for key in request.POST:
            if key.startswith("type_"):
                value = request.POST[key]
                if value is PRECONDITION_TYPE_REQ_ES:
                    var = value
                
                
                
                
            
            # loop through keys and values
                
        return HttpResponseRedirect("/kappa/requirements")
