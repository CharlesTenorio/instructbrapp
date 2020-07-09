import os
from decouple import config
import dj_database_url
from functools import partial
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition
LIB_APPS = [
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'django_extensions',
]

APLICACAO_APPS = [
             'feriados',
              'cidades',
             ]

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = (
    DEFAULT_APPS + LIB_APPS + APLICACAO_APPS
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

ROOT_URLCONF = 'appferiados.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'appferiados.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

parse_database =partial(dj_database_url.parse, conn_max_age=600)

DATABASES = {'default': config('DATABASE_URL', default=default_dburl, cast=parse_database), }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# STORAGE DE CONFIGRUCAO DO AWS
#----------------------------------------------------------------------------
if  AWS_ACCESS_KEY_ID:
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400', }
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_LOAD_METADATA = True
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_CUSTOM_DOMAIN = None
    AWS_DEFAULT_ACL = 'private'
    #Static assets
    #---------------------------------------------------------------------------
    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    STATIC_S3_PATH = 'static'
    STATIC_ROOT = f'/{STATIC_S3_PATH}/'
    STATIC_URL = f'///s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{STATIC_S3_PATH}/'
    ADMIN_MEDIA_PREFIX =  f'///s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{STATIC_S3_PATH}/' + 'admin/'
    # uplaod dos arqivos
    #--------------------------------------------------------------------------

    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = 'media'
    MEDIA_ROOT = f'/{DEFAULT_S3_PATH}/'
    MEDIA_URL = f'///s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{DEFAULT_S3_PATH}/'
    INSTALLED_APPS.append('s3_folder_storage')
    INSTALLED_APPS.append('storages')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'estaticos')
]