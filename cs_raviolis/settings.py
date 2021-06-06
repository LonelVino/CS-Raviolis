"""
Django settings for cs_raviolis project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0t2eg7o57daoy_=)h-g!qe*hr#=m7*^edyt&-7j-u1fs!rqjnn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS=['*']
CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'oauth2_provider',
    'corsheaders',
    'TestModel',
    'api_v1'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # before authentification middleware
    # it will try to authenticate user with the OAuth2 access token and 
    # set request.user and request._cached_user fields 
    # so that AuthenticationMiddleware (when active) will not try to get user from the session. 
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cs_raviolis.urls'

#  we only want to allow cross-origin resource from http://localhost:8080 locally
CORS_ORIGIN_ALLOW_ALL = True    

# CORS_ORIGIN_WHITELIST = (
#     'http://127.0.0.1:8080',   # Frontend on dev mode
#     'http://127.0.0.1:8081',    # Frontend on dev mode
#     'http://localhost:8080', # Frontend on dev mode
#     'http://localhost:8081', # Frontend on dev mode
#     'http://127.0.0.1:8000',   # Backend    
#     'http://localhost:8000', 
#     'https://127.0.0.1:8000',   # Backend    
#     'http://cs-raviolis.herokuapp.com',
#     'https://cs-raviolis.herokuapp.com',
# )


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dist')],
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

WSGI_APPLICATION = 'cs_raviolis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'csRaviolis.db',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    # Uncomment following if you want to access the admin
    'django.contrib.auth.backends.ModelBackend'
)

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dist'),
    os.path.join(BASE_DIR, 'dist/static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 扩展 Model
# AUTH_USER_MODEL = 'info.UserInfo'

options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)

# # clear the DATABASES variable and then set the 'default' key using the dj_database_url module.
# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# OAuth2 Part
# LOGIN_URL='/admin/login/'
# 服务器端
LOGIN_URL='https://auth.viarezo.fr/oauth/authorize/?response_type=code&client_id=9f812cb77e1b92e5943ce4369d4c8ec187905105&redirect_uri=https://cs-clubchinois-raviolis.herokuapp.com/&state=default&scope=default'

# LOGIN_URL='https://auth.viarezo.fr/oauth/authorize/?response_type=code&client_id=9f812cb77e1b92e5943ce4369d4c8ec187905105&redirect_uri=http://127.0.0.1:8000/&state=default&scope=default'

# LOGIN_REDIRECT_URL = '/'