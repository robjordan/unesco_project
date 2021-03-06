"""
Django settings for unesco project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Dealing with environment variables
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """Get the environment variable or return and exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("UNESCO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/tmp/django-debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

ALLOWED_HOSTS = [ 'localhost', ]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
#    'debug_toolbar.apps.DebugToolbarConfig',
    'social.apps.django_app.default',
    'crispy_forms',
    'django_date_extensions',
    'leaflet',
    'whsites',
    'visits',
    'members',
    'registration',
)

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy("members:login")
LOGIN_REDIRECT_URL = reverse_lazy("members:home")
LOGOUT_URL = reverse_lazy("members:logout")
AUTH_USER_MODEL = "auth.User"


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'unesco.urls'

WSGI_APPLICATION = 'unesco.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': get_env_variable("UNESCO_DB_NAME"),
        'USER': get_env_variable("UNESCO_DB_USER"),
        'PASSWORD': get_env_variable("UNESCO_DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
]

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_HOST = get_env_variable("EMAIL_HOST")
EMAIL_PORT = get_env_variable("EMAIL_PORT")
EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = get_env_variable("EMAIL_USE_TLS")

ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window;
REGISTRATION_AUTO_LOGIN = True  # Automatically log the user in.

SITE_ID = '2'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_PATH,
)

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (0, 0),
    'DEFAULT_ZOOM': 1,
    'MIN_ZOOM': 1,
    'MAX_ZOOM': 18,
    'RESET_VIEW': True,

}

# Social Auth configuration
SOCIAL_AUTH_TWITTER_KEY = get_env_variable("UNESCO_SOCIAL_AUTH_TWITTER_KEY")
SOCIAL_AUTH_TWITTER_SECRET = get_env_variable("UNESCO_SOCIAL_AUTH_TWITTER_SECRET")
SOCIAL_AUTH_FACEBOOK_KEY = get_env_variable("UNESCO_SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = get_env_variable("UNESCO_SOCIAL_AUTH_FACEBOOK_SECRET")
SOCIAL_AUTH_FACEBOOK_SCOPE = ['publish_actions', 'email']
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [('username', 'username'), ('name', 'name')]
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_env_variable("UNESCO_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_env_variable("UNESCO_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = [('username', 'username'), ('name', 'name'),('gender','gender'),('emails','emails')]
SOCIAL_AUTH_LOGIN_REDIRECT_URL = reverse_lazy("members:home")
SOCIAL_AUTH_LOGIN_URL = reverse_lazy("members:login")
# SOCIAL_AUTH_NEW_USER_REDIRECT_URL = 

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'members.models.create_member_from_social_profile',
)
