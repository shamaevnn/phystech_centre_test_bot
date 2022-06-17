import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class Environment(Enum):
    production = 'prod'
    development = 'dev'


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

ENVIRONMENT = os.getenv('ENVIRONMENT', Environment.production)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
