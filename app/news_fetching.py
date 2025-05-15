# app/news_fetching.py

import requests
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news_articles(query: str = "latest", page_size: int = 5):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize={page_size}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
