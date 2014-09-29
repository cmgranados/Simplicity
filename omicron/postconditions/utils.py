from omicron.postconditions.models import PostconditionTestCase, \
    PostconditionDescription


def get_postconditions_tc_by_testcase(testcase):
    postcondition_tc_list = PostconditionTestCase.objects.filter(postcondition__postconditiontestcase=testcase.test_case_id)
    return postcondition_tc_list

def get_postconditions_desc_by_testcase(testcase):
    postcondition_desc_list = PostconditionDescription.objects.filter(postcondition__postconditiondescription=testcase.test_case_id)
    return postcondition_desc_list