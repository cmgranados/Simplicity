from kappa.preconditions.models import PreconditionDescription, PreconditionRequirement

def get_preconditions_req_by_req(requirement, precondition_list):
    precondition_requirement_list = PreconditionRequirement.objects.filter(precondition_id = precondition_list)
    return precondition_requirement_list

def get_preconditions_desc_by_req(requirement, precondition_list):
    precondition_description_list = PreconditionDescription.objects.filter(precondition_id = precondition_list)
    return precondition_description_list