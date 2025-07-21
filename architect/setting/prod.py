from architect.settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$eknlti*ji9p$cla7!yrwh+8%cu8nku%%u=73uut)#pyi7_&@8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




STATIC_ROOT= BASE_DIR /'static'


MEDIA_ROOT= BASE_DIR /'media'
STATICFILES_DIRS = [ BASE_DIR /'statics',]

#CSRF_COOKIE_SECURE = True