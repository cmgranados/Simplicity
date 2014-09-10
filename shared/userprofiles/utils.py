from django.contrib.auth.models import Group
from shared.userprofiles.models import UserProfile
from shared.types_simplicity.models import Type


def register_user(group, user, registration_type):
    """
    python auth pipeline function to assign a group to a new user.
    """
    requirement_analyst_group = Group.objects.get(name=group)
    requirement_analyst_group.user_set.add(user)
    requirement_analyst_group.save()

    profile = UserProfile()
    profile.registration_type = Type.objects.get(name=registration_type)
    profile.user = user
    profile.save()
