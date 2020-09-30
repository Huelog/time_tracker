import os


class Config:
    LOG_FILE = os.getenv('LOG_FILE', '~/time_log.csv')
