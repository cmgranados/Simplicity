from datetime import datetime, timedelta
import json
import logging
import time

from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic.list import ListView
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from jira.client import JIRA

from kappa.businessrules.models import BusinessRule
from kappa.preconditions.models import Precondition, PreconditionRequirement, \
    PreconditionDescription
from kappa.requirements.models import Requirement, RequirementBusinessRule,\
    RequirementInput, RequirementOutput, AcceptanceCriteria
from shared.states_simplicity.models import State
from shared.types_simplicity.models import Type, TypeClassification
from simplicity_main.constants import MyConstants
from simplicity_main.settings import STATE_REGISTERED, ACTIVE, \
    PRECONDITION_TYPE_REQ_ES


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

@login_required
def searchRequirements(request):
    if not request.POST.get('q', '') :
        content_auto_v = "descripcion"
    else:
        content_auto_v = request.POST.get('q', '')
        
    requirements = SearchQuerySet().models(Requirement).filter(text=content_auto_v)
    return render_to_response('ajax_requirements_search.html', {'requirements': requirements})

@login_required
def searchBusinessRules(request):
    if not request.POST.get('br', '') :
        content_auto_v = ""
    else:
        content_auto_v = request.POST.get('br', '')
         
    businessrules = SearchQuerySet().models(BusinessRule).filter(text=content_auto_v)
    return render_to_response('ajax_businessrule_search.html', {'businessrules': businessrules})

@login_required
def new_requirement(request):
    constants = MyConstants()
    requirement_type_code = constants.TYPE_CLASSIFICATION_CODE.get(constants.REQUIREMENT_TYPE_CLASSIFICATION_KEY)
    br_type_code = constants.TYPE_CLASSIFICATION_CODE.get(constants.BUSINESS_RULES_TYPE_CLASSIFICATION_KEY)
    type_classification_req = TypeClassification.objects.get(code = requirement_type_code)
    type_classification_br = TypeClassification.objects.get(code = br_type_code)
    requirement_type_list = Type.objects.filter(type_classification_id =
                                                type_classification_req.type_classification_id)
    br_type_list = Type.objects.filter(type_classification_id = 
                                       type_classification_br.type_classification_id)
     
    return render(request, 'requirement_form_base.html', {'requirement_type_list': requirement_type_list, 
                                                          'br_type_list' : br_type_list})

@login_required
def save_requirement_definition(request):
    if request.method == "POST": 
        new_requirement = Requirement()
        
        requirement_title = request.POST.get('requirementTitle', None)
        new_requirement.title = requirement_title
        
        requirement_code = request.POST.get('requirementCode', None)
        new_requirement.code = requirement_code
        
        requirement_date_created = datetime.now()
        new_requirement.date_created = requirement_date_created
        
        requirement_type = request.POST.get('requirementType', None)
        type_retrieved = Type.objects.get(type_id=requirement_type) 
        new_requirement.type = type_retrieved
        
        requirement_description = request.POST.get('requirementDescription', None)
        new_requirement.description = requirement_description
        
        state = State.objects.get(state_id=STATE_REGISTERED) 
        new_requirement.state = state
        new_requirement.date_modified = requirement_date_created
        new_requirement.is_active = ACTIVE
        
        requirement_keywords = request.POST.get('requirementKeywords', None)
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
    
@login_required 
def delete_requirement(request):
    success = True
    if request.POST.get('id', '') :
        id_requirement = request.POST.get('id', '')
        requirement =  Requirement.objects.get(requirement_id = id_requirement)
        deleted_state = State.objects.get(state_id = MyConstants.REQUIREMENT_DELETED_STATE_ID)
        requirement.is_active = '0'
        requirement.state = deleted_state
        requirement.date_modified = datetime.now()
        success =  requirement.save()
    else:
        success = False
         
    return render(request, 'requirements/search.html', {'success': success})


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
        print project.name
        projects.append(jira.project(project.id))
        roles = jira.project_components(project.id)
        users = jira.search_assignable_users_for_projects('ajardila',project.key)
        logger.debug("Cantidad: " + str(users))
    return render_to_response('jira_projects_list.html', {'projects': projects})


def save_requirement_ajax(request):
    if request.method == "POST":
        requirement_str = request.POST.get('requirement', None)
        requirement_dict = json.loads(requirement_str)
        if not requirement_dict:
            message = "error"
            return render_to_response('error.html', {'message': message})
            #return HttpResponseRedirect("error.html")
        else:
            message = "success "
            requirement = Requirement()
            requirement.title = requirement_dict[u'name']
            #requirement.code = requirement_dict[u'code']
            requirement.requirement_date_created = datetime.now()
            requirement.type = Type.objects.get(type_id = requirement_dict[u'type'])
            requirement.description = requirement_dict[u'description']
            state = State.objects.get(state_id=STATE_REGISTERED) 
            requirement.state = state
            requirement.date_modified = datetime.now()
            requirement.date_created = datetime.now()
            requirement.is_active =ACTIVE
            requirement.keywords = requirement_dict[u'keywords']
            requirement.save()
            requirement.code = "RE_" + str(requirement.requirement_id)
            requirement.save()
            save_preconditions(requirement_dict, requirement)
            save_business_rules(requirement_dict, requirement)
            save_information_flow(requirement_dict, requirement)
            save_acceptance_criteria(requirement_dict, requirement)
            return render_to_response('done.html', {'message': message})
            #return HttpResponseRedirect("done.html")
            
def save_preconditions(requirement_dict, requirement):    
    preconditions = requirement_dict[u'preconditions']
    for precondition in preconditions:
        print(precondition[u'type'])
        precondition_tmp = Precondition()
        precondition_tmp.requirement = requirement
        precondition_tmp.save()
        
        if MyConstants.PRECONDITION_TYPE_DESCRIPTION == precondition[u'type']:
            precondition_desc_tmp = PreconditionDescription()
            precondition_desc_tmp.description =  precondition[u'description']
            precondition_desc_tmp.precondition = precondition_tmp
            precondition_desc_tmp.save();
        else:
            precondition_req_tmp = PreconditionRequirement()
            precondition_req_tmp.requirement = requirement
            precondition_req_tmp.precondition = precondition_tmp
            precondition_req_tmp.save();

def save_business_rules(requirement_dict, requirement):
    business_rules_dict = requirement_dict[u'businessRules']
    
    for business_rule in business_rules_dict:
        br = BusinessRule.objects.get(business_rule_id = business_rule[u'id'])
        requirement_business_rule = RequirementBusinessRule()
        requirement_business_rule.requirement = requirement
        requirement_business_rule.business_rule = br
        requirement_business_rule.save()
        
def save_information_flow(requirement_dict, requirement):
    output_dict = requirement_dict[u'outputInformation']
    input_dict = requirement_dict[u'inputInformation']
    
    for ou in output_dict:
        req_output = RequirementOutput()
        req_output.requirement = requirement
        req_output.output = ou[u'value']
        req_output.description = ou[u'description']
        req_output.data_type = ou[u'dataType']
        req_output.save()
        
    for inp in input_dict:
        req_input = RequirementInput()
        req_input.requirement = requirement
        req_input.input = inp[u'value']
        req_input.description = inp[u'description']
        req_input.data_type = inp[u'dataType']
        req_input.save()
        
def save_acceptance_criteria(requirement_dict, requirement):
    acceptance_criteria_dict = requirement_dict[u'acceptanceCriteria']
    
    for crit in acceptance_criteria_dict:
        acceptance_criteria = AcceptanceCriteria()
        acceptance_criteria.requirement = requirement
        acceptance_criteria.name = crit[u'value']
        acceptance_criteria.description = crit[u'description']
        acceptance_criteria.date_modified = datetime.now()
        acceptance_criteria.date_created = datetime.now()
        acceptance_criteria.save()
        acceptance_criteria.code = "CA_" + str(acceptance_criteria.acceptance_criteria_id)
        acceptance_criteria.save()
    
def new_businessrule_ajax(request):
    if request.method == "POST":
        business_rule = BusinessRule()
        newBusinessRuleTitle = request.POST.get('newBusinessRuleTitle', None)
        newBusinessRuleCode = request.POST.get('newBusinessRuleCode', None)
        businessRulesType = request.POST.get('businessRulesType', None)
        newBusinessRuleDescription = request.POST.get('newBusinessRuleDescription', None)
        business_rule.name = newBusinessRuleTitle
        business_rule.code = newBusinessRuleCode
        br_type = Type.objects.get(type_id = businessRulesType)
        business_rule.type = br_type
        business_rule.description = newBusinessRuleDescription
        business_rule.date_created = datetime.now()
        business_rule.date_modified = datetime.now()
        business_rule.state = State.objects.get(state_id=STATE_REGISTERED) 
        business_rule.save()
    return render_to_response('done.html')
        #return HttpResponseRedirect("done.html")
    