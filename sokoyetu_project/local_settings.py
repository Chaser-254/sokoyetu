# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oc^1694%m=5(p*nwz7_hh8ado-d7o9w+)#zj265_rwqml1kdk5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sokoyetu',
        'USER': 'manu',
        'PASSWORD': 'Manu@254#',
        'HOST': 'localhost'
    }
}
