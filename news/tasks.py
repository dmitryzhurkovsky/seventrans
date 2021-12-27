from news.models import Article
from news.parsers import TransInfoParser
from seventrans.celery import app


@app.task
def parse_news_and_populate_database():
    parser = TransInfoParser()

    pages = parser.get_count_of_pages()
    for page in range(pages):
        news = parser.get_news(page_number=page)

        for article in news:
            body_article, publication_date = parser.get_article_date_and_body(article)

            Article.objects.get_or_create(
                title=article.get('title'),
                publish_date=publication_date,
                body=body_article,
                preview_body=article.get('preview_body'),
                img_url=article.get('img_url'),
            )
