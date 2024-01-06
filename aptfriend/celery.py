import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aptfriend.settings')
app = Celery('aptfriend')
app.config_from_object("aptfriend.celery_config")
