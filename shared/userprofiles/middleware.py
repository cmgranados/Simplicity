from django.conf import settings
from django.http import HttpResponseRedirect

from shared.userprofiles.models import UserProfile
from simplicity_main.constants import MyConstants


class LoginValidationMiddleware:
    """
    Middleware wich validates the login type so it won't allow a non SNS\
    registered user to log in with an SNS login (like google+)
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required middleware\
         requires authentication middleware to be installed. Edit your\
         MIDDLEWARE_CLASSES setting to insert\
         'django.contrib.auth.middleware.AuthenticationMiddleware'.\
          If that doesn't work, ensure your TEMPLATE_CONTEXT_PROCESSORS\
           setting includes 'django.core.context_processors.auth'."
        user = request.user
        if not user.is_authenticated():
#             print user.username + " is not Autenticated"
            profile_arr = UserProfile.objects.filter(user__username=user.username)
            if len(profile_arr) > 0:
                profile = profile_arr[0]
                if profile.registration_type.name == MyConstants.REGISTRATION_TYPE_GOOGLE :
                    None
        else:
            print request.user.username + " is Autenticated"

