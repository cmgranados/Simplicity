import logging

from django.shortcuts import render, render_to_response
from haystack.query import SearchQuerySet

from omicron.testcases.models import TestCase


logger = logging.getLogger('simplicity_main.omicron.testcases.views')

def new_test_case(request):    
    return render(request, 'test_case_form_base.html')

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

