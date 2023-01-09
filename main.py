from fake_headers import Headers
import requests
import bs4


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
base_url = 'http://habr.com'
url = base_url + '/ru/all/'
headers = Headers(
    headers=True
).generate()


response = requests.get(url, headers=headers)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all('article')
for article in articles:
    link_ = base_url + article.find('h2').find('a').attrs['href']
    request_full_article = requests.get(link_, headers=headers).text
    soup_full_article = bs4.BeautifulSoup(request_full_article, 'html.parser')
    full_article = soup_full_article.find(class_='tm-article-presenter__body').text
    for word in KEYWORDS:
        if word.lower() in full_article.lower():
            time_ = article.find('time').attrs['datetime'].split('T')[0]
            header_ = article.find('h2').find('span').text
            print(time_ + ' - ' + header_ + ' - ' + link_)
            break
