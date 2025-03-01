import os
import dj_database_url

SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['sokoyetu-app-073a3271922d.herokuapp.com', '127.0.0.1', 'localhost']


DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
}
