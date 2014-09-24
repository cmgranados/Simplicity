<<<<<<< HEAD
import logging
=======
# -*- coding: utf-8 -*-

from datetime import datetime
import json

from django.shortcuts import render, render_to_response

from omicron.postconditions.models import Postcondition
from omicron.preconditions.models import OmPrecondition, \
    OmPreconditionDescription, OmPreconditionTestCase
from omicron.testcases.models import TestCase, TestCaseRequirement, \
    TestCaseInput, TestCaseProcedure, TestCaseUpdateAuthor
from shared.states_simplicity.models import State
from shared.types_simplicity.models import Type
from simplicity_main.constants import MyConstants
from simplicity_main.settings import STATE_REGISTERED, ACTIVE
>>>>>>> 6bce2b5753eb68308c3a44ef86d0edf602ed58e9

from django.shortcuts import render, render_to_response
from haystack.query import SearchQuerySet

from omicron.testcases.models import TestCase


logger = logging.getLogger('simplicity_main.omicron.testcases.views')

def new_test_case(request):    
    return render(request, 'test_case_form_base.html')

<<<<<<< HEAD
def home_test_cases(request):
    testcases = []
    testcases = SearchQuerySet().models(TestCase).load_all()
    return render(request, 'testcase_list.html', {'testcases': testcases})

def search_test_cases(request):
    testcases = []
    logger.debug("searching testcases: ")
    if not request.POST.get('q', '') :
        content_auto_v = "*:*"
        testcases = SearchQuerySet().models(TestCase).load_all()
    else:
        content_auto_v = request.POST.get('q', '')
        logger.debug("searching testcases by: " + content_auto_v)
        testcases = SearchQuerySet().models(TestCase).filter(text=content_auto_v)
        
    return render_to_response('_testcase_result.html', {'testcases': testcases})

=======
def save_test_case_ajax(request):
        try:
            if request.method == "POST":
                test_case_str = request.POST.get('test_case', None)
                test_case_dict = json.loads(test_case_str)
                error = '0'
                if not test_case_dict:
                    raise Exception('test_case_dict_empty', 'test_case_dict_empty')
                else:
                    if  MyConstants.ZERO == test_case_dict[u'test_case_id']:
                        test_case = TestCase()
                        message = "El caso de prueba se guard� correctamente"
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
                    
                    test_case.title = test_case_dict[u'name']
                    #requirement.code = test_case_dict[u'code']
                    test_case.requirement_date_created = datetime.now()
                    test_case.type = Type.objects.get(type_id = test_case_dict[u'type'])
                    test_case.description = test_case_dict[u'description']
                    state = State.objects.get(state_id=STATE_REGISTERED) 
                    test_case.state = state
                    test_case.date_modified = datetime.now()
                    test_case.is_active =ACTIVE
                    test_case.keywords = test_case_dict[u'keywords']
                    test_case.save()
                    test_case.code = "TC_" + str(test_case.requirement_id)
                    test_case.save()
                    save_preconditions(test_case_dict, test_case)
#                     save_business_rules(test_case_dict, test_case)
#                     save_information_flow(test_case_dict, test_case)
#                     save_acceptance_criteria(test_case_dict, test_case)
                    return render_to_response('done.html', {'message': message,'error': error})
        except:
            error = '1'
            message = "Ocurrio un error"
            return render_to_response('done.html', {'message': message,'error': error})

 
def save_preconditions(requirement_dict, test_case):   
    preconditions = requirement_dict[u'preconditions']
    for precondition in preconditions:
        print(precondition[u'type'])
        precondition_tmp = OmPrecondition()
        precondition_tmp.test_case = test_case
        precondition_tmp.save()
        
        if MyConstants.PRECONDITION_TYPE_DESCRIPTION == precondition[u'type']:
            precondition_desc_tmp = OmPreconditionDescription()
            precondition_desc_tmp.description =  precondition[u'description']
            precondition_desc_tmp.precondition = precondition_tmp
            precondition_desc_tmp.save();
        else:
            precondition_req_tmp = OmPreconditionTestCase()
            precondition_req_tmp.test_case = test_case
            precondition_req_tmp.precondition = precondition_tmp
            precondition_req_tmp.save();
>>>>>>> 6bce2b5753eb68308c3a44ef86d0edf602ed58e9