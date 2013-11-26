"""
Django settings for celerydemo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

REDIS_HOST = 'localhost:6379/0'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8r#g+=u56jp@@u4i0dimt$ayplp)*x@$xp0e(4sb-g264)&=f='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0/0']

LANGUAGES = ['en-us']
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'celerymon',
    'celerydemo'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'celerydemo.urls'

WSGI_APPLICATION = 'celerydemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

STATIC_URL = '/static/'


BROKER_URL = 'redis://%s' % REDIS_HOST
CELERY_RESULT_BACKEND = 'redis://%s' % REDIS_HOST
CELERY_ACKS_LATE = True
CELERY_ENABLE_UTC = True
CELERY_ENABLE_REMOTE_CONTROL = True
CELERY_EVENT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERY_MESSAGE_COMPRESSION = 'gzip'
CELERY_SEND_EVENTS = True
CELERY_SEND_TASK_ERROR_EMAILS = False
CELERY_SEND_TASK_SENT_EVENT = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_TASK_RESULT_EXPIRES = 86400
CELERYD_PREFETCH_MULTIPLIER = 2
CELERY_TIMEZONE = 'UTC'
CELERY_TRACK_STARTED = True
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_CHORD_PROPAGATES = True
