from shared.types_simplicity.models import TypeClassification, Type
from simplicity_main.constants import MyConstants


def get_testcase_types():
    constants = MyConstants()
    tc_type_code = constants.TEST_CASE_TYPE_CLASSIFICATION_CODE
    tc_type_classification = TypeClassification.objects.get(code = tc_type_code)
    tc_type_list = Type.objects.filter(type_classification_id = 
                                       tc_type_classification.type_classification_id)
    return tc_type_list