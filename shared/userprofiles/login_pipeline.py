from simplicity_main.constants import MyConstants
from shared.userprofiles.utils import register_user
from shared.userprofiles.models import UserProfile
from django.contrib.auth.models import User
from social.exceptions import AuthAlreadyAssociated


def user_group(backend, user, response, *args, **kwargs):
    """
    Python auth pipeline function to assign a group to a new user.
    """
    # Verify if the user is registering or was already registered
    profile_arr = UserProfile.objects.filter(user=user)
    if len(profile_arr) == 0:
        register_user(MyConstants.GROUP_REQUIREMENT_ANALYST_NAME, user, MyConstants.REGISTRATION_TYPE_GOOGLE)


def login_type_restriction(backend, user, response, *args, **kwargs):

    user_exists_arr = User.objects.filter(email=user.email)
    if len(user_exists_arr) > 0:
        existent_user = user_exists_arr[0]
        # All the existent users should have a UserProfile
        profile = UserProfile.objects.get(user__email=existent_user.email)
        if profile.registration_type.name == MyConstants.REGISTRATION_TYPE_REGULAR:
            raise AuthAlreadyAssociated()
