"""
Django settings for FESSEF project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'icqffoc1-t%up*9l)kpoz-9ow(dx*kl0ar*4j8pp=6ryj4-9mc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    # "django.contrib.admin.apps.SimpleAdminConfig",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# applicatio was installed with pip
THIRD_PARTY_APPS = [
    'six', 
    'taggit',
    'tinymce',
    'ckeditor',
    'colorfield',
    'crispy_forms',
    'social_django',
    'ckeditor_uploader',
    'django_summernote',
    'admin_interface',
    
    
]

# application was installed with django-admin
LOCAL_APPS = [
    'Chats',
    'event',
    'xamxam',
    'evenadmin',
    'reporting',
    'Postfeeds',
    'Competence',
    'AnnonceEtpse',
    'utilisateurs',
    'notifications',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# template for crispy
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# CKEDITOR UPLOAD
CKEDITOR_UPLOAD_PATH = "feseul_image/"

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

AUTH_USER_MODEL = 'utilisateurs.User'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'FESSEF.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',


                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here
                'notifications.views.CountNotifications'
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
    
    'django.contrib.auth.backends.ModelBackend',
)


WSGI_APPLICATION = 'FESSEF.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL  = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/' )
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static/"),
# ]


STATIC_URL = '/static/'
STATICFILES_DIRS = (     
    os.path.join(BASE_DIR, 'static/'), 
) 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# les deux ligne de codes qui fonctionne à part la partie admin
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     BASE_DIR, "static",
#     '/var/www/static/',
# ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media Files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'


# Debutconf pour Summernote
X_FRAME_OPTIONS = 'SAMEORIGIN'
# SUMMERNOTE_THEME = 'bs4'
# fin conf pour Summernote



EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='alphaibrahimas95@gmail.com'
EMAIL_HOST_PASSWORD='alphasow1995##'
EMAIL_USE_TLS=True
EMAIL_PORT=587


from django.contrib.messages import constants as messages
MESSAGE_TAGS={
    messages.ERROR:'danger'
}


SITE_ID = 1

LOGIN_REDIRECT_URL        = 'feseul'
LOGIN_URL                 = 'login'
LOGOUT_REDIRECT_URL       = '/'
LOGOUT_URL                = 'logout'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'GOOGLE_KEY'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'SECRET'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '361006191613077'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '97d0b117c706ca6134c8effbd9235896'  # App Secret

# Twiter
SOCIAL_AUTH_TWITTER_KEY = 'jSxY2C0Od1STCUZGxWM7cqLsn' 
SOCIAL_AUTH_TWITTER_SECRET = 'Fri0j1ue4lB1kgqPO0SeUu0knj7B0mn6G2hWXsID6COoKk5OWK'

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77pdiappawx8d1'       #Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = '84S0ib9BgrFvX8VO'  #Client Secret
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'formatted-name', 'public-profile-url', 'picture-url']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
    ('id', 'id'),
    ('formattedName', 'name'),
    ('emailAddress', 'email_address'),
    ('pictureUrl', 'picture_url'),
    ('publicProfileUrl', 'profile_url'),
]


# Tinymce

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}