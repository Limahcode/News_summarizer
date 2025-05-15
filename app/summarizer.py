from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import newspaper

router = APIRouter()

# Summarization pipeline
summarizer = pipeline("summarization")

# Request body models
class SummaryRequest(BaseModel):
    text: str

class URLRequest(BaseModel):
    url: str

@router.post("/summarize-text")
def summarize_text(request: SummaryRequest):
    try:
        summary = summarizer(request.text, max_length=300, min_length=100, do_sample=False)
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summarize-url")
def summarize_url(request: URLRequest):
    try:
        article = newspaper.Article(request.url)
        article.download()
        article.parse()
        summary = summarizer(article.text, max_length=300, min_length=100, do_sample=False)
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to summarize: {str(e)}")
