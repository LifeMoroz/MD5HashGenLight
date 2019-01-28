import logging

from celery import Celery

from config import CELERY_BACKEND_URL, CELERY_BROKER_URL
from service import MD5HashProcessor
from utils import send_result_to_email

logger = logging.getLogger(__name__)

app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_BACKEND_URL)


@app.task(track_started=True)
def calculate_md5_hash(url, email_to=''):
    """ Celery-task for calculating hash """
    logger.info("Start to process: %s", url)

    if not url:
        raise ValueError(f'Bad url `{url}`')

    hash_processor = MD5HashProcessor()
    hash_value = hash_processor.get_hash_for_url(url),
    if email_to:
        logger.info('Send results to [%s]', email_to)
        send_result_to_email(email_to, str(url), hash_value)

    return hash_value, url
