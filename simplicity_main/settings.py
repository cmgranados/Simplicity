"""
Django settings for simplicity_main project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "shared/templates"),
    os.path.join(BASE_DIR, "shared/templates/home"),
    os.path.join(BASE_DIR, "kappa/templates"),
    os.path.join(BASE_DIR, "kappa/templates/requirements"),
    os.path.join(BASE_DIR, "kappa/templates/businessrules"),
    os.path.join(BASE_DIR, "kappa/templates/home"),
    os.path.join(BASE_DIR, "shared/templates/userprofiles"),
    os.path.join(BASE_DIR, "alfa/templates/projects"),
)

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'shared/static'),
                    os.path.join(BASE_DIR, 'kappa/static'),
                    os.path.join(BASE_DIR, 'alfa/static'), )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$sz2z@6k4k2fdyqxv8ffbmj691^b(^zc)vczbh^!z3jis&0f#s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'south',
    'rest_framework',
    'haystack',
    'kappa.businessrules',
    'kappa.requirements',
    'kappa.preconditions',
    'alfa.projects',
    'shared.states_simplicity',
    'shared.types_simplicity',
    'shared.userprofiles',
    'social.apps.django_app.default',
    'django.contrib.formtools',
    'autofixture',
    'mockups',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'shared.userprofiles.middleware.LoginValidationMiddleware',
)

ROOT_URLCONF = 'simplicity_main.urls'

WSGI_APPLICATION = 'simplicity_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'simplicity',
        'USER': 'simplicity',
        'PASSWORD': 'porteaW1',
        'HOST': 'mysql1.itc.com.co',
     }

#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'simplicity',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#     }
}

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Configure authentication on rest request
REST_FRAMEWORK = {
    #'DEFAULT_PERMISSION_CLASSES': (
    #    'rest_framework.permissions.IsAuthenticated',
    #),
    #'DEFAULT_AUTHENTICATION_CLASSES': (
    #    'rest_framework.authentication.BasicAuthentication',
    #),
    #'DEFAULT_RENDERER_CLASSES': (
        #'rest_framework.renderers.YAMLRenderer',
        #'rest_framework.renderers.BrowsableAPIRenderer',
    #)
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/shared/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    'shared.userprofiles.backends.EmailBackend',
)

LOGIN_REDIRECT_URL = '/'

# aplicaciones@itc.com.co, see installation guide.
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "363982401495-roer8bb6sterf8uk8ana8v154fgrji3c.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "U587jEnWMoXwP1xZ0T3_KuI4"
SOCIAL_AUTH_USER_MODEL = 'auth.User'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'shared.userprofiles.login_pipeline.user_group',
)

SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]

DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'SIMPLICITY.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'simplicity_main': {
            'handlers': ['logfile'],
            'level': 'DEBUG',  # Or maybe INFO or DEBUG
            'propagate': False
        },
    },
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# States for requirements
STATE_REGISTERED = 1

# States for active/inactive
INACTIVE = 0
ACTIVE = 1

# Precondition types: requirement or description
PRECONDITION_TYPE_REQ_ES = "Requisito"

LOGIN_URL = '/'


# Set up for sending emails
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'simplicity@itc.com.co'
EMAIL_HOST_PASSWORD = ''

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# JIRA CONFIGURATION
OPTIONS = {
    'server': 'https://itcsas.atlassian.net',
}

JIRA_ACCESS_TOKEN = 'srkLiVajV2EtYhHhgi2x8DJjpoqSyXaN'
JIRA_ACCESS_TOKEN_SECRET = 'qkjFBvRxAwAZb4ygpTObr1IhJfPmy0h1'
JIRA_CONSUMER_KEY = 'simplicity'
JIRA_PEM_PATH = os.path.join(BASE_DIR, "shared/jira/jira.pem")
