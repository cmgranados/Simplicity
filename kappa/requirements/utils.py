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
    

def get_if_inputs_associated_to_requirement(requirement):
    requirement_input_list = RequirementInput.objects.filter(requirement_id=requirement.requirement_id)
    return requirement_input_list
    
def get_if_outputs_associated_to_requirement(requirement):
    requirement_output_list = RequirementOutput.objects.filter(requirement_id=requirement.requirement_id)
    return requirement_output_list

def get_acceptancecriterias_associated_to_requirement(requirement):
    acceptance_criteria_list = AcceptanceCriteria.objects.filter(requirement_id=requirement.requirement_id)
    return acceptance_criteria_list
