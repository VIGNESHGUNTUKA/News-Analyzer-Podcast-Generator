import os
import json
from datetime import datetime

def save_fetched_news(category, language, articles):
    """
    Saves the fetched news articles along with category, language, headlines and details 
    into a consolidated JSON file located in BackEnd/data/fetched_news.json.
    """
    # Resolve the correct path to BackEnd/data
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(backend_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    
    filepath = os.path.join(data_dir, "fetched_news.json")
    
    # Extract headlines
    headlines = [art.get("title", "") for art in articles if art.get("title")]
    
    # Format news items
    news_items = []
    for art in articles:
        news_items.append({
            "title": art.get("title", ""),
            "description": art.get("description", ""),
            "content": art.get("content", ""),
            "url": art.get("url", ""),
            "publishedAt": art.get("publishedAt", ""),
            "source": art.get("source", {}).get("name", "") if isinstance(art.get("source"), dict) else str(art.get("source", ""))
        })
        
    entry = {
        "timestamp": datetime.now().isoformat(),
        "category": category,
        "language": language,
        "headlines": headlines,
        "news": news_items
    }
    
    # Load existing news if file exists
    existing_data = []
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
                if not isinstance(existing_data, list):
                    existing_data = []
        except Exception as e:
            print(f"Error reading existing fetched_news.json: {e}")
            existing_data = []
            
    existing_data.append(entry)
    
    # Write back to file
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)
        print(f"Successfully saved fetched news to {filepath}")
    except Exception as e:
        print(f"Error saving fetched news to {filepath}: {e}")
