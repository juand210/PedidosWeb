from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO SECRET_KEY = 'django-insecure-9paqn7+#d1r2cd3u+k$j3und%(vc6*^5h2h7sj8x6sif6jrs!i'

# SECURITY WARNING: don't run with debug turned on in production!
# TODO DEBUG = True

# TODO ALLOWED_HOSTS = ['*']


# Application definition


BASE_APPS = [
<<<<<<< HEAD
    'core.apps.CoreConfig'
=======
>>>>>>> 6133edad35565e743e5168cdd11cb9588b2c5eba
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]
LOCAL_APPS = [

]
THIRDS_APPS = [

]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRDS_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
<<<<<<< HEAD
        'BACKEND': 'django.templates.backends.django.DjangoTemplates',
=======
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
>>>>>>> 6133edad35565e743e5168cdd11cb9588b2c5eba
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
<<<<<<< HEAD
                'django.templates.context_processors.debug',
                'django.templates.context_processors.request',
=======
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
>>>>>>> 6133edad35565e743e5168cdd11cb9588b2c5eba
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-col'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/'
