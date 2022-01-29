from datetime import datetime
from datetime import timedelta
from typing import Optional

import requests
from bs4 import BeautifulSoup
# from django.conf import settings

from config import settings  # only for testing!


class BamapParser:
    URL = settings.BAMAP_PARSED_URL
    date_previous_piece_of_news = None

    def get_news(self, page_number: int = 1) -> list:
        response = requests.get(url=self.URL, headers=settings.PARSED_HEADERS, params={'PAGEN_1': page_number})
        soup = BeautifulSoup(response.text, features="html.parser")

        raw_data = soup.find_all('div', {'class': 'item'})
        news = []

        for article in raw_data:
            title = article.find('a').text.strip()
            href = article.find('a').get('href')

            date_element = article.find('div', {'class': 'date'})
            if date_element:
                date = date_element.text

                self.date_previous_piece_of_news = date
            else:
                date = self.date_previous_piece_of_news

            news.append(({'title': title, 'article_url': href[27:], 'date': date}))

        return news

    def get_full_piece_of_news(self, article: dict) -> str:
        response = requests.get(
            self.URL,
            headers=settings.PARSED_HEADERS,
            params={'ELEMENT_ID': article.get('href')}
        )
        soup = BeautifulSoup(response.text, features="html.parser")

        article_body = soup.find('div', {'class': 'p_body'}).text.strip()

        return article_body


class TransInfoParser:
    URL = settings.NEWS_TRANSINFO_PARSED_URL
    COUNT_OF_RECORDS_ON_PAGE = settings.NEWS_TRANSINFO_COUNT_OF_RECORDS_ON_PAGE

    def get_count_of_pages(self) -> int:
        response = requests.get(url=f'{self.URL}/page/1')
        soup = BeautifulSoup(response.text, features="html.parser")
        return int(soup.find('div', {'class': 'pagination_inner'}).contents[-6].text)

    def get_news(self, page_number: int = 1) -> Optional[list]:
        response = requests.get(url=f'{self.URL}/page/{page_number}')
        soup = BeautifulSoup(response.text, features="html.parser")

        raw_data = soup.find_all('div', {'class': 'list-item_inner'})

        news = []

        for article in raw_data[:self.COUNT_OF_RECORDS_ON_PAGE]:

            raw_title = article.find('h2', {'class': 'list-item_title'})
            if raw_title:
                title = raw_title.text

            preview_body = article.find('p', {'class': 'list-item_text'}).text
            img_url = article.find('div', {'class': 'list-item_img'}).a.img.get('src')
            article_url = article.find('h2', {'class': 'list-item_title'}).a.get('href')

            if 'transinfo' in title.lower().split() or 'transinfo' in preview_body.lower().split():
                continue

            body, publish_date = self.get_article_date_and_body(article_url=article_url)

            for word in body:
                if 'transinfo' in word.lower():
                    continue

            news.append({
                'title': title,
                'preview_body': preview_body,
                'img_url': img_url,
                'article_url': article_url,
                'body': ''.join(map(str, body)),
                'publish_date': publish_date

            })

        return news

    def get_article_date_and_body(self, article_url: str) -> (str, datetime):
        response = requests.get(url=article_url)
        soup = BeautifulSoup(response.text, features="html.parser")

        article_body = soup.find('div', {'class': 'news_view__text'}).contents[2:]
        article_body = [row.text.replace(chr(160), ' ') if row != '\n' else '\n' for row in article_body]
        raw_publish_date = soup.find('p', {'class': 'news-view__date'}).span.text[13:]

        raw_date = raw_publish_date.lower().split(', ')[0]
        raw_time = raw_publish_date.lower().split(', ')[1]
        time = datetime.strptime(raw_time, '%H:%M')

        if 'сегодня' in raw_date:
            publish_date = datetime.today()
            publish_date.replace(hour=time.hour, minute=time.minute)

        elif 'вчера' in raw_date:
            publish_date = datetime.today() - timedelta(days=1)
            publish_date.replace(hour=time.hour, minute=time.minute)

        else:
            publish_date = datetime.strptime(raw_publish_date, '%d.%m.%Y, %H:%M')

        return article_body, publish_date

s = TransInfoParser().get_news()