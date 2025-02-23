import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sokoyetu_project.settings')
app = Celery('finesauces_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()