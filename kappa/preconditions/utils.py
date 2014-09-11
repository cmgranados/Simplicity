from kappa.preconditions.models import PreconditionDescription, PreconditionRequirement
from kappa.preconditions.tests import PreconditionRequirementTestCase

def get_preconditions_req_by_req(requirement):
    precondition_requirement_list = PreconditionRequirement.objects.filter(precondition__requirement_id=requirement.requirement_id)
    return precondition_requirement_list

def get_preconditions_desc_by_req(requirement):
    precondition_description_list = PreconditionDescription.objects.filter(precondition__requirement_id=requirement.requirement_id)
    return precondition_description_list