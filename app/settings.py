# coding=utf8
import sys
import environ

root = environ.Path(__file__) - 1
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    KAFKA_BOOTSTRAP_SERVERS=(str, ''),
    KAFKA_CHECK_ONLY=(bool, False),
    KAFKA_AUTO_COMMIT_SYNC=(bool, False),
    KAFKA_AUTO_COMMIT_ASYNC=(bool, False),
)
environ.Env.read_env("./.env")  # reading .env file

SITE_ROOT = root()
DEBUG = env('DEBUG')  # False if not in os.environ

DATABASES = {
    'default': env.db(),
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

DATABASES['default']['CONN_MAX_AGE']=10

CELERY_BROKER_URL = env('CELERY_BROKER_URL')

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 * 3
CELERY_MAX_CACHED_RESULTS = 1
CELERY_TRACK_STARTED = True
CELERY_IGNORE_RESULT = True
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
CELERY_SEND_EVENTS = True
CELERY_SEND_TASK_SENT_EVENT = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYD_MAX_TASKS_PER_CHILD = 10000


public_root = root.path('')

MEDIA_ROOT = public_root('media')
MEDIA_URL = '/media/'
STATIC_ROOT = public_root('static')
STATIC_URL = '/static/'

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'raven.contrib.django.raven_compat',
    'django_extensions',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [SITE_ROOT + "/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
        'sentry': {
            'level': 'ERROR',
            # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            # 'tags': {'custom-tag': 'x'},
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
    },

}

KAFKA_BOOTSTRAP_SERVERS = env('KAFKA_BOOTSTRAP_SERVERS')
KAFKA_AUTO_COMMIT_SYNC = env('KAFKA_AUTO_COMMIT_SYNC')
KAFKA_AUTO_COMMIT_ASYNC = env('KAFKA_AUTO_COMMIT_ASYNC')
KAFKA_CHECK_ONLY = env('KAFKA_CHECK_ONLY')
KAFKA_AUTO_OFFSET_RESET = env('KAFKA_AUTO_OFFSET_RESET')
KAFKA_GROUP = env('KAFKA_GROUP')
