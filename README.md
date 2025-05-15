"""
# 🧠 News Summarization API

This is a simple API-only backend using FastAPI and Hugging Face transformers that summarizes news articles either by:
- Providing a block of text
- Supplying a news article URL

## 🚀 Features
- `/summarize-text`: Summarizes plain article text
- `/summarize-url`: Scrapes and summarizes from a given URL

## 🛠 Tech Stack
- FastAPI
- Hugging Face Transformers
- newspaper3k

## 📦 How to Run

1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the app:
```bash
uvicorn app.main:app --reload
```

3. Visit Swagger UI to test:
```
http://127.0.0.1:8000/docs
```

## 📌 Example
**POST** `/summarize-text`
```json
{
  "text": "Today, the president announced a new initiative to combat climate change..."
}

Response:
{
  "summary": "The president launched a new climate initiative today..."
}
```

## 🌐 Deployment
You can deploy this API using:
- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Heroku (deprecated but still possible)]

## 🙌 Author
Built by LimahCode.
"""
