# -*- coding: utf-8 -*-

from datetime import datetime
import json
import logging

from django.core.paginator import Paginator, InvalidPage
from django.http.response import Http404
from django.shortcuts import render, render_to_response
from haystack.query import SearchQuerySet

from kappa.businessrules.models import BusinessRule
from kappa.requirements.models import RequirementBusinessRule, Requirement
from omicron.postconditions.models import Postcondition, \
    PostconditionDescription, PostconditionTestCase
from omicron.preconditions.models import OmPrecondition, \
    OmPreconditionDescription, OmPreconditionTestCase
from omicron.testcases.models import TestCase, TestCaseRequirement, \
    TestCaseInput, TestCaseProcedure, TestCaseUpdateAuthor
from omicron.testcases.utlis import get_testcase_types, get_sort_options
from shared.states_simplicity.models import State
from shared.types_simplicity.models import Type
from shared.types_simplicity.utils import get_datatypes_types
from simplicity_main import constants, settings
from simplicity_main.constants import MyConstants
from simplicity_main.settings import STATE_REGISTERED, ACTIVE


logger = logging.getLogger('simplicity_main.omicron.testcases.views')
results_per_page = getattr(settings, 'HAYSTACK_SEARCH_RESULTS_PER_PAGE', 10)

def new_test_case(request):    
    test_case_type_list = get_testcase_types();
    datatype_type_list = get_datatypes_types();
    return render(request, 'test_case_form_base.html', {'test_case_type_list': test_case_type_list,
                                                        'dt_type_list' : datatype_type_list})

def save_testcase_ajax(request):
        try:
            if request.method == "POST":
                test_case_str = request.POST.get('testCase', None)
                test_case_dict = json.loads(test_case_str)
                error = '0'
                if not test_case_dict:
                    raise Exception('test_case_dict_empty', 'test_case_dict_empty')
                else:
                    if  MyConstants.ZERO == test_case_dict[u'test_case_id']:
                        test_case = TestCase()
                        message = "El caso de prueba se guardó correctamente"
                        test_case.date_created = datetime.now()
                        test_case.author = request.user
                        test_case_update_author = None
                    else:
                        test_case = TestCase.objects.get( test_case_id=test_case_dict[u'test_case_id'] )
                        OmPrecondition.objects.filter( test_case_id=test_case.test_case_id ).delete()
                        TestCaseRequirement.objects.filter( test_case_id=test_case.test_case_id ).delete()
                        TestCaseInput.objects.filter( test_case_id=test_case.test_case_id ).delete()
                        TestCaseProcedure.objects.filter( test_case_id=test_case.test_case_id ).delete()
                        Postcondition.objects.filter( test_case_id=test_case.test_case_id ).delete()
                        test_case_update_author = TestCaseUpdateAuthor()
                        test_case_update_author.author = request.user
                        test_case_update_author.update_date = datetime.now()
                        test_case_update_author.test_case = test_case
                        test_case_update_author.save()
                        message = "El caso de prueba se actualiz� correctamente"
                    
                    test_case.name = test_case_dict[u'name']
                    #requirement.code = test_case_dict[u'code']
                    test_case.requirement_date_created = datetime.now()
                    test_case.type = Type.objects.get(type_id = test_case_dict[u'type'])
                    test_case.description = test_case_dict[u'description']
                    state = State.objects.get(state_id=STATE_REGISTERED) 
                    test_case.state = state
                    test_case.date_modified = datetime.now()
                    test_case.is_active = ACTIVE
                    test_case.save()
                    test_case.code = "TC_" + str(test_case.test_case_id)
                    test_case.save()
                    save_preconditions(test_case_dict, test_case)
                    save_postconditions(test_case_dict, test_case)
                    save_requirements(test_case_dict, test_case)
                    save_information_params(test_case_dict, test_case)
                    save_procedure(test_case_dict, test_case)
                    return render_to_response('done.html', {'message': message,'error': error})
        except:
            error = '1'
            message = "Ocurrio un error"
            return render_to_response('done.html', {'message': message,'error': error})

 
def save_preconditions(test_case_dict, test_case):   
    preconditions = test_case_dict[u'preconditions']
    for precondition in preconditions:
        print(precondition[u'type'])
        precondition_tmp = OmPrecondition()
        precondition_tmp.test_case = test_case
        precondition_tmp.save()
        
        if MyConstants.TYPE_DESCRIPTION == precondition[u'type']:
            precondition_desc_tmp = OmPreconditionDescription()
            precondition_desc_tmp.description =  precondition[u'description']
            precondition_desc_tmp.precondition = precondition_tmp
            precondition_desc_tmp.save();
        else:
            precondition_tc_tmp = OmPreconditionTestCase()
            precondition_tc_tmp.test_case = test_case
            precondition_tc_tmp.precondition = precondition_tmp
            precondition_tc_tmp.save();


def save_postconditions(test_case_dict, test_case):   
    postconditions = test_case_dict[u'postconditions']
    for postcondition in postconditions:
        print(postcondition[u'type'])
        postcondition_tmp = Postcondition()
        postcondition_tmp.test_case = test_case
        postcondition_tmp.save()
        
        if MyConstants.TYPE_DESCRIPTION == postcondition[u'type']:
            postcondition_desc_tmp = PostconditionDescription()
            postcondition_desc_tmp.description =  postcondition[u'description']
            postcondition_desc_tmp.postcondition = postcondition_tmp
            postcondition_desc_tmp.save();
        else:
            postcondition_tc_tmp = PostconditionTestCase()
            postcondition_tc_tmp.test_case = test_case
            postcondition_tc_tmp.postcondition = postcondition_tmp
            postcondition_tc_tmp.save();
            
    
def save_requirements(test_case_dict, test_case):
    requirements_dict = test_case_dict[u'requirements']
    for requirement in requirements_dict:
        requirement_obj = Requirement.objects.get(requirement_id = requirement[u'id'])
        test_case_requirement = TestCaseRequirement()
        test_case_requirement.requirement = requirement_obj
        test_case_requirement.test_case = test_case
        test_case_requirement.save() 
    

def save_information_params(test_case_dict, test_case):
    input_dict = test_case_dict[u'inputParameters']
    
    for inp in input_dict:
        tc_input = TestCaseInput()
        tc_input.test_case = test_case
        tc_input.input = inp[u'value']
        tc_input.description = inp[u'description']
        tc_input.data_type = Type.objects.get(type_id=inp[u'dataType'])
        tc_input.save()


def save_procedure(test_case_dict, test_case):
    steps_dict = test_case_dict[u'procedureSteps']
    for step in steps_dict:
        tc_step = TestCaseProcedure()
        tc_step.test_case = test_case
        tc_step.step = step[u'value']
        tc_step.activity = step[u'activity']
        tc_step.save()    

            
def home_test_cases(request):
    testcases = []
    test_case_type_list = get_testcase_types();
    sort_options = get_sort_options();
    testcases = SearchQuerySet().models(TestCase).load_all()
    return render(request, 'testcase_list.html', {'testcases': testcases, 'test_case_type_list': test_case_type_list, 'sort_options': sort_options})

def search_test_cases(request):
    logger.debug("searching testcases: ")
    sort_value = "pub_created"
    sqs = []
    testcases = []
    
    if not request.POST.get('q', '') :
        content_auto_v = "*:*"
        sqs = SearchQuerySet().models(TestCase)
    else:
        content_auto_v = request.POST.get('q', '')
        logger.debug("searching testcases by: " + content_auto_v)
        sqs = SearchQuerySet().models(TestCase).filter(text=content_auto_v)
    
     # Check to see if a start_date was chosen.
    if request.POST.get('type', '') and request.POST.get('type', '') != 'default':
        sqs = sqs.filter(type_id__exact=request.POST.get('type', ''))
        
    if request.POST.get('state', ''):
        sqs = sqs.filter(state_id__exact=request.POST.get('state', ''))
        
     # Check to see if a start_date was chosen.
    if request.POST.get('start_date', '') and request.POST.get('end_date', ''):
        sqs = sqs.filter(pub_created__range=[request.POST.get('start_date', '') + constants.MyConstants.ZERO_HOURS, 
                                             request.POST.get('end_date', '') + constants.MyConstants.ZERO_HOURS])
    
    
    if request.POST.get('sort', ''):
        if str(request.POST.get('sort', '')) == 'desc':
            sort_value = "-pub_created"
            
    testcases = sqs.all()
    (paginator, page) = build_page(request, testcases)
    context = {
        'page': page,
        'paginator': paginator,
    }
    return render_to_response('_testcase_result.html', context)
    #return render_to_response('_testcase_result.html', {'paginator': paginator, 'page': page})

def build_page(request, results):
        try:
            page_no = int(request.POST.get('pageIndex', 1))
        except (TypeError, ValueError):
            raise Http404("Not a valid number for page.")

        if page_no < 1:
            raise Http404("Pages should be 1 or greater.")

        start_offset = (page_no - 1) * results_per_page
        results[start_offset:start_offset + results_per_page]

        paginator = Paginator(results, results_per_page)

        try:
            page = paginator.page(page_no)
        except InvalidPage:
            raise Http404("No such page!")

        return (paginator, page)
