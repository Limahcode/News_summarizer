# from fastapi import APIRouter, HTTPException
# from dotenv import load_dotenv

# import requests
# import os

# # Load the .env file
# load_dotenv()
# router = APIRouter()

# # Ideally store your API key in environment variables
# NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# @router.get("/news")
# def fetch_news(q: str = "latest"):
#     url = f"https://newsapi.org/v2/everything?q={q}&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise HTTPException(status_code=500, detail="Failed to fetch news")


# app/news_api.py
# app/news_api.py

from fastapi import APIRouter, HTTPException, Query
from app.news_fetching import fetch_news_articles
from app.news_processor import process_query

router = APIRouter()

# 🔹 Simple news fetch endpoint
@router.get("/news")
def fetch_news(q: str = "latest"):
    result = fetch_news_articles(query=q)
    if result:
        return result
    else:
        raise HTTPException(status_code=500, detail="Failed to fetch news")

# 🔹 Smart summarization + NER-based news endpoint
@router.get("/smart-news")
def smart_news(q: str = Query(..., description="Search query like 'Osinachi husband case in Nigeria'")):
    try:
        result = process_query(q)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Smart query processing failed: {str(e)}")
