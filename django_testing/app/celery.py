from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_testing.settings")

BASE_REDIS_URL = os.environ.get("REDIS_URL")
app = Celery("django_testing")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks()
app.conf.broker_url = BASE_REDIS_URL
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

app.conf.beat_schedule = {
    "add-every-minute-contrab": {
        "task": "multiply_two_numbers",
        "schedule": crontab(hour=0, minute=1, day_of_week=1),
        "args": (16, 16)
    },
    'add-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': 5.0,
        'args': (16, 16)
    },
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
