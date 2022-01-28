from django.conf import settings
from django.db.models import QuerySet


def modify_len_title_and_body_of_news(news: QuerySet) -> list:
    news = news.values()
    first_article = news[0]
    second_article = news[1]
    third_article = news[2]

    first_article['title'] = first_article.get('title')[:settings.NEWS_INDEX_PAGE_FIRST_ARTICLE_TITLE_LENGTH]
    first_article['preview_body'] = first_article.get('preview_body')[:settings.NEWS_INDEX_PAGE_FIRST_ARTICLE_PREVIEW_BODY_LENGTH]

    second_article['title'] = second_article.get('title')[:settings.NEWS_INDEX_PAGE_SECOND_ARTICLE_TITLE_LENGTH]
    second_article['preview_body'] = second_article.get('preview_body')[:settings.NEWS_INDEX_PAGE_SECOND_ARTICLE_PREVIEW_BODY_LENGTH]

    third_article['title'] = third_article.get('title')[:settings.NEWS_INDEX_PAGE_THIRD_ARTICLE_TITLE_LENGTH]
    third_article['preview_body'] = third_article.get('preview_body')[:settings.NEWS_INDEX_PAGE_THIRD_ARTICLE_PREVIEW_BODY_LENGTH]

    return [first_article, second_article, third_article]


def modify_preview_body_of_news(news: list) -> list:
    for article in news:
        preview_body = article.get('preview_body')



        article['preview_body'] = modify_preview_body

    return news