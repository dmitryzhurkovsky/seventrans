import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from news.tasks import parse_news_and_populate_database

parse_news_and_populate_database()