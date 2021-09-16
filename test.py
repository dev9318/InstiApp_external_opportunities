import requests
import feedparser

url = "http://127.0.0.1:8000/blog/feed"
response = requests.get(url)

feeds = feedparser.parse(response.content)

print(feeds)