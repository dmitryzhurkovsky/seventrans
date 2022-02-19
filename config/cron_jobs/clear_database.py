import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from news.tasks import delete_news_older_than_three_months

delete_news_older_than_three_months()