from pathlib import Path
import os
from dotenv import load_dotenv


# Loading environment variables from ./.env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jk-&*^%5e6ms7sf&_!g7&7(3_9t^!%t)4t7o1)30wksv2^!wy+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SERVER_IP = os.getenv('SERVER_IP') 

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', SERVER_IP]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'botapp',
    'webapp',
    'taskmanager',
    'core'
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

ROOT_URLCONF = 'configs.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'configs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main': {
            'format': '[{levelname}] [{asctime}] - {module} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'common': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "../logs/common.log"),
            'formatter': 'main'
        },
        'botapp': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "../logs/botapp.log"),
            'formatter': 'main'
        },
        'taskmanager': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "../logs/taskmanager.log"),
            'formatter': 'main'
        }
    },
    'loggers': {
        'botapp': {
            'handlers': ['common', 'botapp'],
            'level': 'INFO',
            'propagate': True
        },
        'webapp': {
            'handlers': ['common'],
            'level': 'WARNING',
            'propagate': True
        },
        'taskmanager': {
            'handlers': ['common', 'taskmanager'],
            'level': 'INFO',
            'propagate': True
        },
        'core': {
            'handlers': ['common'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'


TOKEN = os.getenv('VK_API_KEY')
CONFIRM_STR = os.getenv('CONFIRMATION_STR')

VK_APP_ID = os.getenv('VK_APP_ID')
VK_SECRET_KEY = os.getenv('VK_SECRET_KEY')

VK_API_VERSION = '5.122'
VK_API_ENDPOINT = 'https://api.vk.com/method/'
VK_OAUTH_URL = 'http://oauth.vk.com/authorize'

REDIRECT_URL = SERVER_IP + "/auth"
