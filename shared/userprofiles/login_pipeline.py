from simplicity_main.constants import MyConstants
from shared.userprofiles.utils import register_user
from shared.userprofiles.models import UserProfile


def user_group(backend, user, response, *args, **kwargs):
    """
    Python auth pipeline function to assign a group to a new user.
    """
    # Verify if the user is registering or was already registered
    profile_arr = UserProfile.objects.filter(user=user)
    if len(profile_arr) == 0:
        register_user(MyConstants.GROUP_REQUIREMENT_ANALYST_NAME, user, MyConstants.REGISTRATION_TYPE_GOOGLE)
