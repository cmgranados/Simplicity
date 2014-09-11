from kappa.businessrules.models import BusinessRule


def get_businessrules_associated_to_requirement(requirement):
    br_list = BusinessRule.objects.filter(requirementbusinessrule__requirement_id=requirement.requirement_id)
    return br_list
