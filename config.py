# celery config
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_BACKEND_URL = 'redis://localhost:6379/1'

# mail config
MAIL_SERVER = 'smtp.gmail.com'
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_PORT = 587

# directory for files
DOWNLOAD_PATH = ''
PORT = 8080


try:  # Override settings by local configuration
    from local_settings import *  # NOQA: F403, F401
except ImportError:
    pass
