"""
Django settings for scrum project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
import os
from pathlib import Path
from dotenv import load_dotenv
import graphql

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

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
    'django.contrib.staticfiles',
    
    #    3rd party app
    'graphene_django',
    'graphql_auth',
    'django_filters',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
     
        # custom apps
    'apps.project_management',
    'apps.authentication_app',
    
]
AUTH_USER_MODEL = 'authentication_app.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'scrum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'scrum.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT':os.environ.get('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Graphene schema
GRAPHENE = {
    "SCHEMA": "scrum.schema",
        'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    # optional
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
}

GRAPHQL_AUTH = {
    'LOGIN_ALLOWED_FIELDS': ['email', 'email'],
    'ALLOW_LOGIN_NOT_VERIFIED': True,
    'ALLOW_LOGIN_WITH_SECONDARY_EMAIL':True,
    'ALLOW_PASSWORDLESS_REGISTRATION':False,
    'ALLOW_DELETE_ACCOUNT':False,
    'SEND_ACTIVATION_EMAIL':True,
    'SEND_PASSWORD_SET_EMAIL':False,
    'REGISTER_MUTATION_FIELDS':['email', 'email'],
    'REGISTER_MUTATION_FIELDS_OPTIONAL':[],
    'UPDATE_MUTATION_FIELDS':["first_name", "last_name"],
    'CUSTOM_ERROR_TYPE':'graphql_auth.types.ExpectedErrorType',  
    'USER_NODE_FILTER_FIELDS':{
    "email": ["exact",],
    "username": ["exact", "icontains", "istartswith"],
    "is_active": ["exact"],
    "status__archived": ["exact"],
    "status__verified": ["exact"],
    "status__secondary_email": ["exact"],
},
    'USER_NODE_EXCLUDE_FIELDS':["password", "is_superuser"],
    'EXPIRATION_ACTIVATION_TOKEN':timedelta(days=7),
    'EXPIRATION_PASSWORD_RESET_TOKEN':timedelta(hours=1),
    'EXPIRATION_SECONDARY_EMAIL_ACTIVATION_TOKEN':timedelta(hours=1),
    'EXPIRATION_PASSWORD_SET_TOKEN':timedelta(days=7),
    'EMAIL_FROM':'nuel@email.com',
    'ACTIVATION_PATH_ON_EMAI':'activate',
    'PASSWORD_RESET_PATH_ON_EMAIL':'password-reset',
    'PASSWORD_SET_PATH_ON_EMAIL':"password-set",
    'ACTIVATION_SECONDARY_EMAIL_PATH_ON_EMAIL':"activate",
    "EMAIL_ASYNC_TASK": "path/to/file.graphql_auth_async_email",
    'EMAIL_SUBJECT_ACTIVATION':'email/activation_subject.txt',
    'EMAIL_SUBJECT_ACTIVATION_RESEND':"email/activation_subject.txt",
    "EMAIL_SUBJECT_SECONDARY_EMAIL_ACTIVATION":"email/activation_subject.txt",
    "EMAIL_SUBJECT_PASSWORD_RESET":"email/password_reset_subject.txt",
    'EMAIL_SUBJECT_PASSWORD_SET':"email/password_set_subject.txt",
    'EMAIL_TEMPLATE_ACTIVATION':"email/activation_email.html",
    'EMAIL_TEMPLATE_ACTIVATION_RESEND':"email/activation_email.html",
    'EMAIL_TEMPLATE_SECONDARY_EMAIL_ACTIVATION':"email/activation_email.html",
    'EMAIL_TEMPLATE_PASSWORD_RESET':"email/password_reset_email.html",
    'EMAIL_TEMPLATE_PASSWORD_SET':"email/password_set_email.html",
        "EMAIL_TEMPLATE_VARIABLES": {
        "frontend_domain": "the-frontend.com"
    },
     
    
}

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
SENDER_EMAIL = os.environ.get('SENDER_EMAIL')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
