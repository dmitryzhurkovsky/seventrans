import requests
from bs4 import BeautifulSoup

# from django.conf import settings
from seventrans import settings  # todo - only for test


class BamapParser:
    URL = settings.BAMAP_PARSED_URL
    date_previous_piece_of_news = None

    def get_news(self, page_number: int = 1) -> list:
        response = requests.get(url=self.URL, headers=settings.PARSED_HEADERS, params={'PAGEN_1': page_number})
        soup = BeautifulSoup(response.text, features="html.parser")

        raw_data = soup.find_all('div', {'class': 'item'})
        news = []

        for piece_of_news in raw_data:
            title = piece_of_news.find('a').text.strip()
            href = piece_of_news.find('a').get('href')

            date_element = piece_of_news.find('div', {'class': 'date'})
            if date_element:
                date = date_element.text

                self.date_previous_piece_of_news = date
            else:
                date = self.date_previous_piece_of_news

            news.append(({'title': title, 'href': href[27:], 'date': date}))

        return news

    def get_full_piece_of_news(self, piece_of_news: dict) -> dict:
        response = requests.get(
            self.URL,
            headers=settings.PARSED_HEADERS,
            params={'ELEMENT_ID': piece_of_news.get('href')}
        )
        soup = BeautifulSoup(response.text, features="html.parser")

        piece_of_news_text = soup.find('div', {'class': 'p_body'}).text.strip()
        piece_of_news['body'] = piece_of_news_text

        return piece_of_news


class TransInfoParser:
    URL = settings.NEWS_TRANSINFO_PARSED_URL
    COUNT_OF_RECORDS_ON_PAGE = settings.NEWS_TRANSINFO_COUNT_OF_RECORDS_ON_PAGE

    def get_count_of_pages(self) -> int:
        response = requests.get(url=f'{self.URL}/page/1')
        soup = BeautifulSoup(response.text, features="html.parser")
        return int(soup.find('div', {'class': 'pagination_inner'}).contents[-6].text)

    def get_news(self, page_number: int = 1) -> list:
        response = requests.get(url=f'{self.URL}/page/{page_number}')
        soup = BeautifulSoup(response.text, features="html.parser")

        raw_data = soup.find_all('div', {'class': 'list-item_inner'})
        news = []

        for piece_of_news in raw_data[:self.COUNT_OF_RECORDS_ON_PAGE]:
            title = piece_of_news.find('h2', {'class': 'list-item_title'}).text
            date = piece_of_news.find('p', {'class': 'list-item_date'}).text
            short_body_text = piece_of_news.find('p', {'class': 'list-item_text'}).text
            img_url = piece_of_news.find('div', {'class': 'list-item_img'}).a.img.get('src')
            piece_of_news_url = piece_of_news.find('h2', {'class': 'list-item_title'}).a.get('href')

            news.append({
                'title': title,
                'date': date,
                'short_body_text': short_body_text,
                'img_url': img_url,
                'piece_of_news_url': piece_of_news_url
            })

        return news

    def get_full_piece_of_news(self, piece_of_news: dict) -> dict:
        url = piece_of_news.get('piece_of_news_url')
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, features="html.parser")

        piece_of_news_text = soup.find('div', {'class': 'news_view__text'}).text.strip()
        piece_of_news['body'] = piece_of_news_text

        return piece_of_news

