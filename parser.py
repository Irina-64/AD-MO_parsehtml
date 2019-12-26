"""Пример работы с beautifulsoup"""
# 1. регулярные выражения
# 2. сторонние библиотеки beautifulsoup, lxml
# 3. scrapy
import requests
from bs4 import BeautifulSoup

url = 'http://dedmorozural.ru/novosti'

response = requests.get(url)

# print(response.status_code)

# print(response.text)

# Создаем суп для разбора html
soup = BeautifulSoup(response.text, 'html.parser')

# Получаем тег title
# print(soup.title)

# bs4.element.Tag
# print(type(soup.title))

# Через точку мы находим первый тег
# print(soup.a)

# Чтобы получить текст внутри тега
# print(soup.a.string)
# строка str
# print(soup.a.text)
# bs4.element.NavigableString
# print(type(soup.a.string))
# print(type(soup.a.text))

# атрибут
# print(soup.a.get('href'))

# Находим все картинки
# images_tags = soup.find_all('img')
#
# for image_tag in images_tags:
#     print(image_tag)

# Поиск по классу - Обычно самое полезное!!!

big_body_div = soup.find('div', class_='modulebody1')

# print(big_body_div)
# print(type(big_body_div))
# print(big_body_div.get('class'))

# 1. Лучший вариант искать тожде по классу
# Можно искать в уже найденном
# modulebody3 = big_body_div.find('div', class_='modulebody3')
# print(modulebody3)

# 2. Если не получается найти по классу или по тегу, то придется по порядку
# .contents

# print(big_body_div.contents)
# print(len(big_body_div.contents))
# находим ссылку a по порядку
# print(big_body_div.contents[1].contents[1].contents)

# modulebody 1
print(big_body_div.prettify())
# modulebody 2
print(big_body_div.contents[1])
# modulebody 3
print(big_body_div.contents[1].contents[1])

# Получение своих детей
for child in big_body_div.children:
    print(1)
    print(child)

# Рекурсивное получение детей
for child in big_body_div.descendants:
    print(0)
    # print(child)

print(len(list(big_body_div.children)))
print(len(list(big_body_div.descendants)))