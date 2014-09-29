# -*- coding: utf-8 -*-
from omicron.testcases.models import TestCaseRequirement, TestCaseInput, \
    TestCaseProcedure
from shared.types_simplicity.models import TypeClassification, Type
from simplicity_main.constants import MyConstants


def get_testcase_types():
    constants = MyConstants()
    tc_type_code = constants.TEST_CASE_TYPE_CLASSIFICATION_CODE
    tc_type_classification = TypeClassification.objects.get(code = tc_type_code)
    tc_type_list = Type.objects.filter(type_classification_id = 
                                       tc_type_classification.type_classification_id)
    return tc_type_list

def get_sort_options():
    NEWER = 'desc'
    OLDER = 'asc'
    SORT_OPTIONS = (
                (NEWER , 'Más nuevo'),
                (OLDER , 'Más viejo'))
    return SORT_OPTIONS

def get_requirements_by_testcase(testcase):
    requirements_list = TestCaseRequirement.objects.filter(test_case_id=testcase.test_case_id)
    return requirements_list

def get_information_params_by_testcase(testcase):
    info_params_list = TestCaseInput.objects.filter(test_case_id=testcase.test_case_id)
    return info_params_list

def get_procedure_steps_by_testcase(testcase):
    procedure_steps_list = TestCaseProcedure.objects.filter(test_case_id=testcase.test_case_id)
    return procedure_steps_list