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
    os.path.join(BASE_DIR, "shared/templates"), os.path.join(BASE_DIR, "kappa/templates")
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
    'haystack',
    'kappa.businessrules',
    'kappa.requirements',
    'kappa.preconditions',
    'shared.states_simplicity',
    'shared.types_simplicity',
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
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'simplicity',
        'USER': 'simplicity',
        'PASSWORD': 'porteaW1',
        'HOST': 'mysql1.itc.com.co',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/shared/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
