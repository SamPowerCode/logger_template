import logging
import logging.config
from datetime import datetime
import os


logs_dir = 'logs'
log_filename = datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.log")
log_datetime_dir = datetime.now().strftime("%Y-%m-%d")
full_log_path = os.path.join(logs_dir, log_datetime_dir)

if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

if not os.path.exists(full_log_path):
        os.makedirs(full_log_path)


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,  # Keeps existing loggers (important in larger apps)

    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': f'{full_log_path}/{log_filename}',
            'mode': 'a',  # Append mode
        },
    },

    'loggers': {
        'MY_LOGGER': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    }
}


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('MY_LOGGER')


logger.debug("This is a debug message")      # File only
logger.info("This is an info message")       # Console + file
logger.warning("This is a warning message")  # Console + file
logger.error("This is an error message")
logger.critical("This is a critical message")

