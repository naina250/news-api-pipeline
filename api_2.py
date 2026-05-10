import requests
import csv

your_api = "your_api_here"
topic = "lifestyle"

# fetch news
url = "https://newsapi.org/v2/everything"
params = {"q": topic, "apikey": your_api, "pageSize": 50, "language": "en"}

data = requests.get(url, params=params).json()
articles = data["articles"]
print(articles)

# save csv
with open("lifestyle_news.csv", "w", newline="", encoding="utf-8") as file:
	writer = csv.DictWriter(file, fieldnames=['source', 'author', 'title', 'description', 'url', 'published_at'])
	writer.writeheader()
	for a in articles:
		writer.writerow({
			'source': a['source']['name'],
			'author': a.get('author', ''),
			'title': a.get('title', ''),
			'description': a.get('description', ''),
			'url': a.get('url', ''),
			'published_at': a.get('publishedAt', '')
		})

print(f"Done! Saved {len(articles)} articles to lifestyle_news.csv")
