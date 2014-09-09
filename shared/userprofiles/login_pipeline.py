from django.contrib.auth.models import Group
from simplicity_main.constants import MyConstants


def user_group(backend, user, response, *args, **kwargs):
    """
    python auth pipeline function to assign a group to a new user.
    """
    requirement_analyst_group = Group.objects.get(name=MyConstants.GROUP_REQUIREMENT_ANALYST_NAME)
    requirement_analyst_group.user_set.add(user)
    requirement_analyst_group.save()
