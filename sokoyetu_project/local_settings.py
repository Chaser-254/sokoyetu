import os

SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")

DEBUG = os.getenv('DEBUG', 'False') == 'True'



ALLOWED_HOSTS = ["127.0.0.1", "sokoyetu-app-073a3271922d.herokuapp.com", "localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME", "sokoyetu"),
        'USER': os.getenv("DB_USER", "manu"),
        'PASSWORD': os.getenv("DB_PASSWORD", "Manu@254#"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}
