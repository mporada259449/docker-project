from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')

app = Celery('django_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
