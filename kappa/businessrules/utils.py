
rom kappa.businessrules.models import BusinessRule
from shared.types_simplicity.models import TypeClassification, Type
from simplicity_main.constants import MyConstants


def get_businessrules_associated_to_requirement(requirement):
    br_list = BusinessRule.objects.filter(requirementbusinessrule__requirement_id=requirement.requirement_id)
    return br_list

def get_businessrules_types():
    constants = MyConstants()
    br_type_code = constants.BUSINESS_RULE_TYPE_CLASSIFICATION_CODE
    type_classification_br = TypeClassification.objects.get(code = br_type_code)
    br_type_list = Type.objects.filter(type_classification_id = 
                                       type_classification_br.type_classification_id)
    return br_type_list
