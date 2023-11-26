from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
import  calculator.calculator
#import django_app.settings
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')
redis = os.environ.get("REDISADDRESS")
database = os.environ.get("DBADDRESS")
app = Celery('django_app', broker = redis, backend=database)
#app.config_from_object('django_app.settings', namespace='CELERY')
app.autodiscover_tasks(related_name="calculator")