# # app/news_processor.py
# import requests
# from transformers import pipeline
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Load NER and Summarization pipelines
# ner = pipeline("ner")
# summarizer = pipeline("summarization")

# NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# def extract_keywords_from_query(query):
#     entities = ner(query)
#     if not entities:
#     # keywords = [entity['word'] for entity in entities]
#     # return keywords or query.split()  # fallback if no NER entities found
#         return query.split()  # fallback to splitting query
#     return [entity['word'] for entity in entities]


# def fetch_news_from_api(search_query):
#     url = f"https://newsapi.org/v2/everything?q={search_query}&pageSize=3&language=en&apiKey={NEWS_API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json().get("articles", [])
#     return []

# def summarize_article(text):
#     summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
#     return summary[0]['summary_text']

# # def process_query(query):
# #     keywords = extract_keywords_from_query(query)
# #     search_query = " ".join(keywords)
# #     articles = fetch_news_from_api(search_query)

# #     results = []
# #     for article in articles:
# #         content = article.get("content") or article.get("description") or ""
# #         if content:
# #             summary = summarize_article(content)
# #             results.append({
# #                 "title": article.get("title"),
# #                 "summary": summary,
# #                 "url": article.get("url")
# #             })
# #     return results or [{"message": "No relevant news found."}]


# def process_query(query):
#     print("🔍 User query:", query)

#     keywords = extract_keywords_from_query(query)
#     print("🟡 Extracted keywords:", keywords)

#     search_query = " ".join(keywords)
#     print("🔵 Final search query sent to NewsAPI:", search_query)

#     articles = fetch_news_from_api(search_query)
#     print(f"📰 Found {len(articles)} articles from NewsAPI.")

#     results = []
#     for article in articles:
#         content = article.get("content") or article.get("description") or ""
#         print("📄 Article content snippet:", content[:100])
#         if content:
#             summary = summarize_article(content)
#             results.append({
#                 "title": article.get("title"),
#                 "summary": summary,
#                 "url": article.get("url")
#             })

#     if not results:
#         print("❌ No summaries created.")
#         return [{"message": "No relevant news found."}]

#     return results

# app/news_processor.py
import requests
from transformers import pipeline
from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv(dotenv_path="C:/projects/news-summarizer-api/.env")


# Get API key from environment
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# ✅ Print it only after defining it
print("🔐 Loaded API Key:", NEWS_API_KEY)

# Load transformers pipelines
ner = pipeline("ner")
summarizer = pipeline("summarization")



def extract_keywords_from_query(query):
    print("🔍 Original query:", query)
    entities = ner(query)
    print("🟡 NER entities:", entities)

    if not entities:
        fallback = query.split()
        print("⚠️ No NER entities found. Fallback keywords:", fallback)
        return fallback
    
    keywords = [entity['word'] for entity in entities]
    print("✅ Extracted keywords:", keywords)
    return keywords

def fetch_news_from_api(search_query):
    print("🔵 Sending NewsAPI request with:", search_query)
    url = f"https://newsapi.org/v2/everything?q={search_query}&pageSize=3&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    print("🔁 NewsAPI response code:", response.status_code)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        print(f"📄 NewsAPI returned {len(articles)} articles.")
        return articles
    else:
        print("❌ NewsAPI error:", response.text)
        return []

def summarize_article(text):
    print("📝 Summarizing article...")
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def process_query(query):
    keywords = extract_keywords_from_query(query)
    search_query = " ".join(keywords)
    
    articles = fetch_news_from_api(search_query)

    results = []
    for i, article in enumerate(articles):
        content = article.get("content") or article.get("description") or ""
        print(f"📌 Article {i+1} content (first 100 chars):", content[:100])

        if content:
            try:
                summary = summarize_article(content)
                results.append({
                    "title": article.get("title"),
                    "summary": summary,
                    "url": article.get("url")
                })
            except Exception as e:
                print(f"⚠️ Summarization failed: {e}")

    if not results:
        print("❗ No summaries created. Returning default message.")
        return [{"message": "No relevant news found."}]
    
    print(f"✅ Successfully summarized {len(results)} article(s).")
    return results
