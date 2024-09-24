"""
Django settings for ShawaziLandSystem project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import json
import os
from dotenv import load_dotenv, find_dotenv
import dj_database_url
from pathlib import Path
from google.cloud import vision





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b0%bbu$l)0pn*$y*497bs_uhu^ym&_mz8ak1qg_n=bn@!ns1yp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'api',
    'agreements',
    'rest_framework',
    'landDetails',
    'transactions',
    'chatroom',
    'channels',
    'users',
    'land_buyers',
    'land_sellers',
    'lawyers',
    'corsheaders',
    'drf_yasg',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]



CORS_ALLOW_ALL_ORIGINS = True
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ROOT_URLCONF = 'ShawaziLandSystem.urls'

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



WSGI_APPLICATION = 'ShawaziLandSystem.wsgi.application'
ASGI_APPLICATION = 'ShawaziLandSystem.asgi.application'
CHANNEL_LAYERS = {
   
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"},
}



# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}
# Fallback for local development and test environments
if not os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }





# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

OPENSTREETMAP_API_TOKEN = os.getenv('OPENSTREETMAP_API_TOKEN',"")

SMSLEOPARD_API_URL = os.getenv('SMSLEOPARD_API_URL',"")
SMSLEOPARD_ACCESS_TOKEN = os.getenv('SMSLEOPARD_ACCESS_TOKEN',"")

load_dotenv()

GOOGLE_VISION_CREDENTIALS = json.loads(os.getenv('GOOGLE_VISION_CREDENTIALS','{}'))



ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN","")
AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID","")
AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET","")
REDIRECT_URI=os.environ.get("REDIRECT_URI","")
AUTH_USER_MODEL = 'users.CustomUser'
AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )

