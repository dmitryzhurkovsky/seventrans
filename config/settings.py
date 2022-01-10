import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUG = int(os.getenv('DJANGO_DEBUG'))
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'news',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJAGNO_DB_ENGINE', 'django.db.backends.sqlite3'),
        'OPTIONS': {'sql_mode': 'traditional', },
        'NAME': os.getenv('DJAGNO_DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('DJAGNO_DB_USER'),
        'PASSWORD': os.getenv('DJAGNO_DB_PASSWORD'),
        'HOST': os.getenv('DJAGNO_DB_HOST'),
        'PORT': os.getenv('DJAGNO_DB_PORT'),
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# STATIC_ROOT = '/home/a7transb/repositories/seventrans/static/'
# MEDIA_ROOT = '/home/a7transb/repositories/seventrans/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'config', 'static/')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BAMAP_PARSED_URL = 'http://bamap.org/engver/rtnews'

NEWS_TRANSINFO_PARSED_URL = 'https://news.transinfo.by/perevozki'
NEWS_TRANSINFO_COUNT_OF_RECORDS_ON_PAGE = 12

PARSED_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
