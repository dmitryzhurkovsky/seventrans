from news.models import Article
from news.parsers import TransInfoParser


def parse_news_and_populate_database(pages: int = 2) -> None:
    parser = TransInfoParser()

    articles = Article.objects.all()
    if not articles:
        pages = parser.get_count_of_pages()

    for page in range(pages):
        news = parser.get_news(page_number=page)

        for article in news:
            body_article, publication_date = parser.get_article_date_and_body(article_url=article['article_url'])

            Article.objects.get_or_create(
                title=article['title'],
                publish_date=publication_date,
                body=body_article,
                preview_body=article['preview_body'],
                img_url=article['img_url'],
            )
