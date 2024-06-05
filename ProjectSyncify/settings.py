import environ
from datetime import timedelta
from pathlib import Path
from urllib.parse import urlparse
import dj_database_url
env=environ.Env(
    DEBUG=(bool,False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR/'.env')


# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fuhz)@l)976_$+z7moq825_w#4_@dpm4y-sw3wlw3+t2z9xify'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "daphne",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'accounts',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'social_accounts',
    'user',
    'chat',
    'workspace',
    'userprofile',
]

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

ROOT_URLCONF = 'ProjectSyncify.urls'

CORS_ORIGIN_ALLOW_ALL = True
CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1','https://project-syncify.netlify.app','https://projectsyncifyapi.onrender.com','http://localhost:5173']
CORS_ALLOW_ALL_ORIGINS: True
ALLOWED_HOSTS = ["*"]

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

ASGI_APPLICATION = 'ProjectSyncify.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sifathislam790$default',  # Your database name
#         'USER': 'sifathislam790',           # Your database username
#         'PASSWORD': 'sifath2002',           # Your database password
#         'HOST': 'sifathislam790.mysql.pythonanywhere-services.com',  # Your database host
#         'PORT': '3306',                     # The default MySQL port
#     }
# }

AUTH_USER_MODEL='accounts.User'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=360),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD= env("EMAIL_PASSWORD")


GOOGLE_CLIENT_ID=env('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET=env("GOOGLE_CLIENT_SECRET")
GITHUB_CLIENT_ID=env('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET=env('GITHUB_CLIENT_SECRET')
SOCIAL_AUTH_PASSWORD=env('SOCIAL_AUTH_PASSWORD')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REDIS_URL = 'redis://red-cpcm9ka1hbls73c8l3lg:6379'
parsed_url = urlparse(REDIS_URL)
           #* For Production *#
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(
                parsed_url.hostname,
                parsed_url.port,
                {
                    "password": parsed_url.password,
                }
            )],
        },
    },
}

                    #* For localHost *#
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("127.0.0.1", 6379)],
#         },
#     },
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'syncify',
#         'USER': 'teamtechbuilders',
#         'PASSWORD': '1jD2SscWh3VtGMvep3cDeg4haREjykS5',
#         'HOST': 'dpg-cpcmb663e1ms73f092k0-a',
#         'PORT': '5432',
#     }
# }

DATABASE_URL='postgres://teamtechbuilders:1jD2SscWh3VtGMvep3cDeg4haREjykS5@dpg-cpcmb663e1ms73f092k0-a.oregon-postgres.render.com/syncify'
DATABASES = {
	"default": dj_database_url.parse("postgres://teamtechbuilders:1jD2SscWh3VtGMvep3cDeg4haREjykS5@dpg-cpcmb663e1ms73f092k0-a.oregon-postgres.render.com/syncify")
}