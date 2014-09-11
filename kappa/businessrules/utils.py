from kappa.preconditions.models import PreconditionRequirement

def get_businessrules_associated_to_requirement(requirement):
    br_list = PreconditionRequirement.objects.get(requirement_id=requirement.requirement_id)
    return br_list