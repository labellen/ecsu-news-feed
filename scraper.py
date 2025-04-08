import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.easternct.edu"
NEWS_URL = f"{BASE_URL}/news/index.html"

response = requests.get(NEWS_URL)
soup = BeautifulSoup(response.text, 'html.parser')

articles = []

for card in soup.select('.card'):
    title = card.select_one('h3.card-title')
    summary = card.select_one('p.card-text')
    link = card.select_one('a')
    image = card.select_one('img')

    if not all([title, summary, link, image]):
        continue

    article = {
        "title": title.text.strip(),
        "summary": summary.text.strip(),
        "link": BASE_URL + link['href'],
        "imageURL": BASE_URL + image['src']
    }
    articles.append(article)

with open("feed.json", "w") as f:
    json.dump(articles[:5], f, indent=2)
