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

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "shared/templates"), 
    os.path.join(BASE_DIR, "kappa/templates"),
    os.path.join(BASE_DIR, "shared/templates/userprofiles"), 
)

STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'shared/static'), )


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
    'kappa.businessrules',
    'kappa.requirements',
    'kappa.preconditions',
    'shared.states_simplicity',
    'shared.types_simplicity',
    'social.apps.django_app.default',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'simplicity_main.urls'

WSGI_APPLICATION = 'simplicity_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
             
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'simplicity',
#        'USER': 'simplicity', 
#        'PASSWORD': 'porteaW1',
#        'HOST': 'mysql1.itc.com.co',
#     }

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'simplicity',
        'USER': 'root', 
        'PASSWORD': 'root',
        'HOST': 'localhost',
    }
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

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

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
)

LOGIN_REDIRECT_URL = '/welcome.html'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "289278710538-utbdbbmfcg9b0999ed2g7v4mm8fb5q5u.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "CEZmuDvD6LJNLjprNQmysVHl"
