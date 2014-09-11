from django.http import HttpResponseRedirect
from django.conf import settings


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
        if not request.user.is_authenticated():
            print request.usr + "Is not Autenticated"
        else:
            print request.usr + "Is Autenticated"

