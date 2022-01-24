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
            Article.objects.get_or_create(
                title=article['title'],
                publish_date=article['publish_date'],
                body=article['body'],
                preview_body=article['preview_body'],
                img_url=article['img_url'],
            )
