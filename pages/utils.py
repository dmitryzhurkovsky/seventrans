from django.conf import settings
from django.db.models import QuerySet


def modify_len_title_and_body_of_news(news: QuerySet) -> list:
    news = news.values()
    first_article = news[0]
    second_article = news[1]
    third_article = news[2]

    first_article['title'] = first_article.get('title')[:settings.NEWS_INDEX_PAGE_FIRST_ARTICLE_TITLE_LENGTH]

    second_article['title'] = second_article.get('title')[:settings.NEWS_INDEX_PAGE_SECOND_ARTICLE_TITLE_LENGTH]
    second_article['body'] = second_article.get('body')[:settings.NEWS_INDEX_PAGE_SECOND_ARTICLE_BODY_LENGTH]

    third_article['title'] = third_article.get('title')[:settings.NEWS_INDEX_PAGE_THIRD_ARTICLE_TITLE_LENGTH]
    third_article['body'] = third_article.get('body')[:settings.NEWS_INDEX_PAGE_THIRD_ARTICLE_BODY_LENGTH]

    return [first_article, second_article, third_article]
