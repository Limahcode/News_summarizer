
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import FileResponse
# from fastapi.staticfiles import StaticFiles
# from app import auth
# from app.schemas import TextInput, URLInput, SummaryOutput
# from app.summarizer import summarize_text
# from app import database
# from app.auth import router as auth_router  # ✅ NEW
# from app.summarizer import router as summarizer_router  # ✅ NEW
# import newspaper
# import os

# app = FastAPI()

# # ✅ Initialize the database (creates tables)
# database.init_db()

# # Serve static files from the "app" directory (or wherever your index.html is located)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")  # This route will serve the index.html file
# async def serve_home():
#     # Serve the index.html when the root URL is accessed
#     return FileResponse("static/index.html")

# @app.post("/summarize-text", response_model=SummaryOutput)
# def summarize_from_text(data: TextInput):
#     try:
#         summary = summarize_text(data.text)
#         return {"summary": summary}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/summarize-url", response_model=SummaryOutput)
# def summarize_from_url(data: URLInput):
#     try:
#         article = newspaper.Article(data.url)
#         article.download()
#         article.parse()
#         summary = summarize_text(article.text)
#         return {"summary": summary}
#     except Exception as e:
#         raise HTTPException(status_code=400,detail=f"Failed to summarize: {str(e)}")

# # ✅ NEW: Add authentication routes
# app.include_router(auth.router)

# # ✅ NEW: Add summary-saving routes (we’ll build these next)
# app.include_router(summarizer_router)


from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app import auth
from fastapi.middleware.cors import CORSMiddleware
from app import database
from app.auth import router as auth_router
from app.summarizer import router as summarizer_router
from app.news_api import router as news_router

import os

app = FastAPI()


# ✅ Initialize the database (creates tables)
database.init_db()

# Serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def serve_home():
    return FileResponse("app/static/index.html")

# ✅ Authentication routes
app.include_router(auth_router)

# ✅ Summary routes (text + URL)
app.include_router(summarizer_router)

app.include_router(news_router)

