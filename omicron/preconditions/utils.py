from omicron.preconditions.models import OmPreconditionTestCase, \
    OmPreconditionDescription


def get_preconditions_tc_by_testcase(testcase):
    precondition_tc_list = OmPreconditionTestCase.objects.filter(precondition__ompreconditiontestcase=testcase.test_case_id)
    return precondition_tc_list

def get_preconditions_desc_by_testcase(testcase):
    precondition_desc_list = OmPreconditionDescription.objects.filter(precondition__ompreconditiondescription=testcase.test_case_id)
    return precondition_desc_list