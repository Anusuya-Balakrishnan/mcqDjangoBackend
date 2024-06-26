"""
Django settings for mcqProject project.

Generated by 'django-admin startproject' using Django 4.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


from pathlib import Path
# import os
# import django_heroku
# import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*524hw%#q*vjo38ghff!t&jf2u=assbkzeeexysm0ycyye$643'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app','127.0.0.1']


# Application definition

INSTALLED_APPS = ['rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "myapp.apps.MyappConfig",
    "mcqadmin.apps.McqadminConfig",
    'corsheaders',
    # "knox",
    "rest_framework.authtoken"
    
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # Other settings...
} 
# this dictionary added for knox library

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'knox.auth.TokenAuthentication',
#     ),
# }

# AUTHENTICATION_CLASSES = ['knox.auth.TokenAuthentication']

# AUTHENTICATION_BACKENDS = [
#     'myapp.emailAuthenticate.EmailBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://mcqfrontend.vercel.app",
    "https://mcqbackend.vercel.app",
]
ROOT_URLCONF = 'mcqProject.urls'

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

WSGI_APPLICATION = 'mcqProject.wsgi.application'

# WSGI_APPLICATION = 'mcqProject.wsgi.application'
# WSGI_APPLICATION = WSGI_APPLICATION + ':application'

TIMEOUT = 600  # Timeout in seconds


# Database


# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'ENFORCE_SCHEMA': True,
#         'NAME': 'MCQDjangoProject',
#         'HOST': 'localhost',  # MongoDB server address
#         'PORT': 27017,        # MongoDB port number
#     }
# }





DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'MCQDjangoProject',
        'CLIENT':{
            'host': "mongodb+srv://Anusuya:Anusuya07@cluster0.rhwqd.mongodb.net/?retryWrites=true&w=majority",
        },
        'ENFORCE_SCHEMA': True,
        }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

DJONGO_DEBUG = True
# DEBUG = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL='myapp.CustomUser'

APPEND_SLASH = False

# STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')

# STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)
# django_heroku.settings(locals())