import requests
from bs4 import BeautifulSoup as BS

url = 'https://akipress.org'
response = requests.get(url)


if response.status_code == 200:
    soup = BS(response.text, 'html.parser')

    news_title = soup.find_all('a', class_='newslink')

    for headline in news_title:
        news_text = headline.get_text()
        print(news_text)

