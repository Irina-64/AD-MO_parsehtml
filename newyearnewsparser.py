import requests
from bs4 import BeautifulSoup
import pprint

domain = 'http://dedmorozural.ru'
url = f'{domain}/novosti'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

result = {}
news_a = soup.find_all('a', class_='con_titlelink')
for one_news_a in news_a:
    text = one_news_a.text
    href = one_news_a.get('href')
    # print(text, href)
    # шаг 2
    url = f'{domain}{href}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # получаем заголовки
    news_titles_tag = soup.find_all('strong')
    titles = []
    for title_tag in news_titles_tag:
        # print(title_tag.text)
        titles.append(title_tag.text)

    # добавим в словарь
    result[text] = titles

pprint.pprint(result)
