import os
import sys
import json
import traceback
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Project root (two levels up from BackEnd/src/)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add BackEnd/src to Python path so modules can be imported cleanly
backend_src_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, backend_src_dir)

# Import existing backend modules
from config import STOP_WORDS, voices
from textcleaner import cleaner
from frequencyanalizer import freq, most_freq_word, top_5_words
from keywordextractor import extract_keyword
from categorydetector import detect_category
from ReportForManualNews import generate_report_for_manual
from summerize import summarize
from translator import translation
from texttospeech import generate_audio
from newscollector import collect_news
from newsbreif import articles_to_text
from ReportForAutomaticNews import generate_report_for_automatic

# Initialize FastAPI app
app = FastAPI(
    title="NewsPod API",
    description="Backend API for Multilingual News Podcast Generator",
    version="1.0.0"
)

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure output directories exist
os.makedirs(os.path.join(PROJECT_ROOT, "output", "Report"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "output", "Podcast"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "output", "Bookmarks"), exist_ok=True)


# --- Request Models (Pydantic) ---
class ManualNewsRequest(BaseModel):
    text: str
    language: str = "English"
    lang_code: str = "en"
    voice: str = "en-US-ChristopherNeural"


class AutomaticNewsRequest(BaseModel):
    category: str = "Sports"
    language: str = "English"
    lang_code: str = "en"
    voice: str = "en-US-ChristopherNeural"


class BookmarkRequest(BaseModel):
    filename: str


# --- API Routes ---

@app.get("/api/headlines")
def get_headlines():
    categories = ['sports', 'technology', 'general', 'health', 'business', 'politics', 'entertainment', 'science', 'world']
    all_headlines = []

    for cat in categories:
        filepath = os.path.join(PROJECT_ROOT, 'BackEnd', 'data', f'{cat}_news.json')
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    articles = data.get('articles', [])
                    for art in articles[:5]:
                        pub_time = art.get('publishedAt', '')
                        time_str = "Recent"
                        if pub_time:
                            try:
                                dt = datetime.strptime(pub_time, "%Y-%m-%dT%H:%M:%SZ")
                                time_str = dt.strftime("%b %d, %Y - %I:%M %p")
                            except:
                                time_str = pub_time

                        all_headlines.append({
                            'title': art.get('title', 'No Title'),
                            'description': art.get('description', ''),
                            'url': art.get('url', '#'),
                            'image': art.get('image', ''),
                            'source': art.get('source', {}).get('name', 'Unknown'),
                            'publishedAt': time_str,
                            'category': cat.capitalize()
                        })
            except Exception as e:
                print(f"Error loading {filepath}: {e}")

    return all_headlines


@app.post("/api/generate/manual")
def generate_manual(req: ManualNewsRequest):
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="News text cannot be empty.")

    try:
        cleaned = cleaner(text)
        words = cleaned.lower().split()
        dictionary = freq(words, STOP_WORDS)
        freq_word, count = most_freq_word(dictionary)
        sorted_words = top_5_words(dictionary)
        keyword_lis = extract_keyword(sorted_words)
        winner = detect_category(keyword_lis)

        summary = summarize(text, keyword_lis)
        translated_summary = translation(summary, req.lang_code)

        generate_report_for_manual(
            len(words),
            len(dictionary),
            keyword_lis[:5],
            winner,
            freq_word,
            req.language,
            translated_summary,
        )

        audio_path = generate_audio(translated_summary, winner, req.language, req.lang_code, req.voice)

        return {
            "success": True,
            "category": winner,
            "summary": translated_summary,
            "audio_path": audio_path
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/generate/automatic")
def generate_automatic(req: AutomaticNewsRequest):
    try:
        articles, result = collect_news(req.category)
        if result == 0 or not articles:
            raise HTTPException(status_code=404, detail="No news articles found for this category.")

        if result > 20:
            result = 20

        summary = articles_to_text(articles, req.category, result)
        translated_summary = translation(summary, req.lang_code)

        generate_report_for_automatic(req.category, req.language, len(articles), translated_summary)
        audio_path = generate_audio(translated_summary, [req.category], req.language, req.lang_code, req.voice)

        return {
            "success": True,
            "category": req.category,
            "summary": translated_summary,
            "audio_path": audio_path,
            "total_articles": len(articles)
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/podcasts")
def list_podcasts():
    podcast_dir = os.path.join(PROJECT_ROOT, "output", "Podcast")
    podcasts = []

    if os.path.exists(podcast_dir):
        files = [f for f in os.listdir(podcast_dir) if f.endswith('.mp3')]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(podcast_dir, x)), reverse=True)

        for file in files:
            filepath = os.path.join(podcast_dir, file)
            mtime = os.path.getmtime(filepath)
            date_str = datetime.fromtimestamp(mtime).strftime("%b %d, %Y - %I:%M %p")

            category = "General"
            language = "English"
            clean_name = file.replace("['", "").replace("']", "")

            if "NewsPodcast" in clean_name:
                parts = clean_name.split("NewsPodcast_")
                category = parts[0].replace("News", "")
                if len(parts) > 1:
                    lang_parts = parts[1].split("_")
                    language = lang_parts[0]
            elif "Podcast" in clean_name:
                parts = clean_name.split("Podcast")
                category = parts[0]

            podcasts.append({
                "filename": file,
                "url": f"/api/audio/{file}",
                "date": date_str,
                "category": category,
                "language": language
            })

    return podcasts


@app.get("/api/audio/{filename}")
def serve_audio(filename: str):
    file_path = os.path.join(PROJECT_ROOT, 'output', 'Podcast', filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mpeg")
    raise HTTPException(status_code=404, detail="Audio file not found")


@app.get("/api/bookmarks")
def get_bookmarks():
    bookmarks_file = os.path.join(PROJECT_ROOT, "output", "Bookmarks", "bookmarks.json")
    if os.path.exists(bookmarks_file):
        try:
            with open(bookmarks_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading bookmarks: {e}")
    return []


@app.post("/api/bookmarks/toggle")
def toggle_bookmark_api(req: BookmarkRequest):
    filename = os.path.basename(req.filename)
    podcast_dir = os.path.join(PROJECT_ROOT, "output", "Podcast")
    bookmarks_dir = os.path.join(PROJECT_ROOT, "output", "Bookmarks")
    bookmarks_json = os.path.join(bookmarks_dir, "bookmarks.json")

    os.makedirs(bookmarks_dir, exist_ok=True)

    existing = []
    if os.path.exists(bookmarks_json):
        try:
            with open(bookmarks_json, "r", encoding="utf-8") as f:
                existing = json.load(f)
                if not isinstance(existing, list):
                    existing = []
        except Exception:
            existing = []

    is_bookmarked = any(b.get("filename") == filename for b in existing)

    src_audio = os.path.join(podcast_dir, filename)
    dst_audio = os.path.join(bookmarks_dir, filename)

    if is_bookmarked:
        existing = [b for b in existing if b.get("filename") != filename]
        if os.path.exists(dst_audio):
            try:
                os.remove(dst_audio)
            except Exception:
                pass
        action = "removed"
    else:
        if os.path.exists(src_audio):
            import shutil
            shutil.copy2(src_audio, dst_audio)

        category = "General"
        language = "English"
        clean_name = filename.replace("['", "").replace("']", "")
        if "NewsPodcast" in clean_name:
            parts = clean_name.split("NewsPodcast_")
            category = parts[0].replace("News", "")
            if len(parts) > 1:
                lang_parts = parts[1].split("_")
                language = lang_parts[0]
        elif "Podcast" in clean_name:
            parts = clean_name.split("Podcast")
            category = parts[0]

        entry = {
            "filename": filename,
            "url": f"/api/audio/bookmarks/{filename}",
            "date": datetime.now().strftime("%b %d, %Y - %I:%M %p"),
            "category": category,
            "language": language
        }
        existing.append(entry)
        action = "added"

    with open(bookmarks_json, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=4, ensure_ascii=False)

    return {"success": True, "action": action, "bookmarks": existing}


@app.get("/api/audio/bookmarks/{filename}")
def serve_bookmark_audio(filename: str):
    file_path = os.path.join(PROJECT_ROOT, 'output', 'Bookmarks', filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mpeg")
    fallback_path = os.path.join(PROJECT_ROOT, 'output', 'Podcast', filename)
    if os.path.exists(fallback_path):
        return FileResponse(fallback_path, media_type="audio/mpeg")
    raise HTTPException(status_code=404, detail="Bookmark audio file not found")


# Mount UI static files at root AFTER all API routes
app.mount("/", StaticFiles(directory=os.path.join(PROJECT_ROOT, "UI"), html=True), name="ui")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
