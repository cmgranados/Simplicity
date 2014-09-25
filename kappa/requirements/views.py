# -*- coding: utf-8 -*-

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
import ipdb
from jira.client import JIRA

from kappa.businessrules.models import BusinessRule
from kappa.businessrules.utils import get_businessrules_associated_to_requirement, \
    get_businessrules_types
from kappa.preconditions.models import Precondition, PreconditionRequirement, \
    PreconditionDescription
from kappa.preconditions.utils import  \
    get_preconditions_req_by_req, get_preconditions_desc_by_req
from kappa.requirements.models import Requirement, RequirementBusinessRule, \
    RequirementInput, RequirementOutput, AcceptanceCriteria, \
    RequirementUpdateAuthor
from kappa.requirements.utils import get_requirement_types, \
    get_if_inputs_associated_to_requirement, \
    get_if_outputs_associated_to_requirement, \
    get_acceptancecriterias_associated_to_requirement
from shared.states_simplicity.models import State
from shared.types_simplicity.models import Type, TypeClassification
from shared.types_simplicity.utils import get_datatypes_types
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
        content_auto_v = "*:*"
    else:
        content_auto_v = request.POST.get('q', '')
    requirements = SearchQuerySet().models(Requirement).filter(text=content_auto_v)
    return render_to_response('ajax_requirements_search.html', {'requirements': requirements})

@login_required
def searchBusinessRules(request):
    if not request.POST.get('br', '') :
        content_auto_v = "*:*"
    else:
        content_auto_v = request.POST.get('br', '')
         
    businessrules = SearchQuerySet().models(BusinessRule).filter(text=content_auto_v)
    return render_to_response('ajax_businessrule_search.html', {'businessrules': businessrules})

def new_requirement(request):
    
    requirement_type_list = get_requirement_types();
    br_type_list = get_businessrules_types();
    datatype_type_list = get_datatypes_types();
    return render(request, 'requirement_form_base.html', {'requirement_type_list': requirement_type_list, 
                                                          'dt_type_list' : datatype_type_list, 
                                                          'br_type_list' : br_type_list })
    
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
        try:
            if request.method == "POST":
                requirement_str = request.POST.get('requirement', None)
                requirement_dict = json.loads(requirement_str)
                error = '0'
                if not requirement_dict:
                    raise Exception('requirement_dict_empty', 'requirement_dict_empty')
                else:
                    if  MyConstants.ZERO == requirement_dict[u'requirement_id']:
                        requirement = Requirement()
                        message = "Requisito se guardó correctamente"
                        requirement.date_created = datetime.now()
                        requirement.author = request.user
                        requirementUpdateAuthor = None
                    else:
                        requirement = Requirement.objects.get( requirement_id=requirement_dict[u'requirement_id'] )
                        Precondition.objects.filter( requirement_id=requirement.requirement_id ).delete()
                        RequirementBusinessRule.objects.filter( requirement_id=requirement.requirement_id ).delete()
                        RequirementInput.objects.filter( requirement_id=requirement.requirement_id ).delete()
                        RequirementOutput.objects.filter( requirement_id=requirement.requirement_id ).delete()
                        AcceptanceCriteria.objects.filter( requirement_id=requirement.requirement_id ).delete()
                        requirementUpdateAuthor = RequirementUpdateAuthor()
                        requirementUpdateAuthor.author = request.user
                        requirementUpdateAuthor.update_date = datetime.now()
                        requirementUpdateAuthor.requirement = requirement
                        requirementUpdateAuthor.save()
                        message = "Requisito se actualizó correctamente"
                    
                    requirement.title = requirement_dict[u'name']
                    #requirement.code = requirement_dict[u'code']
                    requirement.requirement_date_created = datetime.now()
                    requirement.type = Type.objects.get(type_id = requirement_dict[u'type'])
                    requirement.description = requirement_dict[u'description']
                    state = State.objects.get(state_id=STATE_REGISTERED) 
                    requirement.state = state
                    requirement.date_modified = datetime.now()
                    requirement.is_active =ACTIVE
                    requirement.keywords = requirement_dict[u'keywords']
                    requirement.save()
                    requirement.code = "RE_" + str(requirement.requirement_id)
                    requirement.save()
                    save_preconditions(requirement_dict, requirement)
                    save_business_rules(requirement_dict, requirement)
                    save_information_flow(requirement_dict, requirement)
                    save_acceptance_criteria(requirement_dict, requirement)
                    return render_to_response('done.html', {'message': message,'error': error})
        except:
            error = '1'
            message = "Ocurrio un error"
            return render_to_response('done.html', {'message': message,'error': error})
            
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
        req_output.data_type = Type.objects.get(type_id = ou[u'dataType'])
        req_output.save()
        
    for inp in input_dict:
        req_input = RequirementInput()
        req_input.requirement = requirement
        req_input.input = inp[u'value']
        req_input.description = inp[u'description']
        req_input.data_type = Type.objects.get(type_id=inp[u'dataType'])
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

def update_requirement(request):
    if request.method == "GET": 
        requirement_id_param = request.GET.get('requirementID', '')
        requirement = Requirement.objects.get(requirement_id = requirement_id_param)
        requirement_type_list = get_requirement_types();
        br_type_list = get_businessrules_types();
        precondition_req_associated_list = get_preconditions_req_by_req(requirement);
        precondition_desc_associated_list = get_preconditions_desc_by_req(requirement);
        businessrule_associated_list = get_businessrules_associated_to_requirement(requirement);
        if_input_associated_list = get_if_inputs_associated_to_requirement(requirement);
        if_output_associated_list = get_if_outputs_associated_to_requirement(requirement);
        acceptancecriteria_associated_list = get_acceptancecriterias_associated_to_requirement(requirement);
        datatype_type_list = get_datatypes_types();
        return render(request, 'requirement_form_base.html', {'requirement': requirement, 
                                                              'requirement_type_list': requirement_type_list, 
                                                              'br_type_list' : br_type_list,
                                                              'precondition_req_associated_list': precondition_req_associated_list,
                                                              'precondition_desc_associated_list': precondition_desc_associated_list,
                                                              'businessrule_associated_list': businessrule_associated_list,
                                                              'if_input_associated_list': if_input_associated_list,
                                                              'if_output_associated_list': if_output_associated_list,
                                                              'acceptancecriteria_associated_list': acceptancecriteria_associated_list,
                                                              'dt_type_list' : datatype_type_list,
                                                              }) 

