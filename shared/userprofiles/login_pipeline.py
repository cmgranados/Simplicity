from simplicity_main.constants import MyConstants
from shared.userprofiles.utils import register_user


def user_group(backend, user, response, *args, **kwargs):
    """
    python auth pipeline function to assign a group to a new user.
    """
    register_user(MyConstants.GROUP_REQUIREMENT_ANALYST_NAME, user, MyConstants.REGISTRATION_TYPE_GOOGLE)
