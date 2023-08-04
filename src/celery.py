from celery.schedules import crontab
from httpx import ReadTimeout

from celery import Celery

from src.models import session
from src.services.update_contacts import update_contact
from src.config import settings


app = Celery("contact", backend=settings.uri_redis_connection, broker=settings.uri_redis_connection)


@app.task(
    autoretry_for=(ReadTimeout,),
    retry_backoff=True,
    retry_kwargs={'max_retries': 3}
)
def runner():
    with session() as dbsession:
        update_contact(dbsession)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(day_of_month=1), runner.s(), name='Start updater'
    )
