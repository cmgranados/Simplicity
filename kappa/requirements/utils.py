from shared.types_simplicity.models import TypeClassification, Type
from simplicity_main.constants import MyConstants
from kappa.requirements.models import RequirementInput, RequirementOutput,\
    AcceptanceCriteria


def get_requirement_types():
    constants = MyConstants()
    requirement_type_code = constants.REQUIREMENT_TYPE_CLASSIFICATION_CODE
    type_classification_req = TypeClassification.objects.get(code = requirement_type_code)
    requirement_type_list = Type.objects.filter(type_classification_id =
                                                type_classification_req.type_classification_id)
    return requirement_type_list
    
    

def get_businessrules_types():
    constants = MyConstants()
    br_type_code = constants.BUSINESS_RULE_TYPE_CLASSIFICATION_CODE
    type_classification_br = TypeClassification.objects.get(code = br_type_code)
    br_type_list = Type.objects.filter(type_classification_id = 
                                       type_classification_br.type_classification_id)
    return br_type_list

def get_datatypes_types():
    constants = MyConstants()
    dt_type_code = constants.DATATYPE_TYPE_CLASSIFICATION_CODE
    type_classification_dt = TypeClassification.objects.get(code = dt_type_code)
    dt_type_list = Type.objects.filter(type_classification_id = 
                                       type_classification_dt.type_classification_id)
    return dt_type_list
    

def get_if_inputs_associated_to_requirement(requirement):
    requirement_input_list = RequirementInput.objects.filter(requirement_id=requirement.requirement_id)
    return requirement_input_list
    
def get_if_outputs_associated_to_requirement(requirement):
    requirement_output_list = RequirementOutput.objects.filter(requirement_id=requirement.requirement_id)
    return requirement_output_list

def get_acceptancecriterias_associated_to_requirement(requirement):
    acceptance_criteria_list = AcceptanceCriteria.objects.filter(requirement_id=requirement.requirement_id)
    return acceptance_criteria_list