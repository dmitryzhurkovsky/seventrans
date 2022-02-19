import datetime

from news.models import Article
from news.parsers import TransInfoParser


def parse_news_and_populate_database(pages: int = 3) -> None:
    parser = TransInfoParser()

    for page in range(pages):
        news = parser.get_news(page_number=page)

        for article in news:
            Article.objects.get_or_create(
                title=article['title'],
                publish_date=article['publish_date'],
                body=article['body'],
                preview_body=article['preview_body'],
                img_url=article['img_url'],
            )


def delete_news_older_than_three_months() -> None:
    three_month_earlier_date = datetime.datetime.now() - datetime.timedelta(days=90)
    Article.objects.filter(publish_date__lt=three_month_earlier_date).delete()
