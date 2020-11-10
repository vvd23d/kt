import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kt.settings')

SCHEDULE = os.environ.get("SCHEDULE", default='10')
minute = '*/' + str(SCHEDULE)


celery_app = Celery('kt')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "task-will-start-few-minutes": {
        "task": "main.tasks.load_btc",
        "schedule": crontab(minute=minute)
    }
}
