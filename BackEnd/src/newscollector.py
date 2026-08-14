import requests
from dotenv import load_dotenv
import os
import json

# LOAD ENVIRONMENT VARIABLES

load_dotenv()

api_key = os.getenv("GNEWS_API_KEY")


def collect_news(category):

    url = (
        f"https://gnews.io/api/v4/top-headlines?"
        f"category={category.lower()}&"
        f"lang=en&"
        f"country=in&"
        f"max=10&"
        f"apikey={api_key}"
    )

    response = requests.get(url)

    print("Status Code:", response.status_code)

    data = response.json()

    # HANDLE API ERRORS

    if response.status_code != 200:
        print("API Error:", data.get("errors", "Unknown error"))
        return [], 0

    # GET ARTICLES

    articles = data.get("articles", [])

    print("Total Articles Received:", data.get("totalArticles", 0))
    print("Articles Retrieved:", len(articles))

    # REMOVE DUPLICATE ARTICLES

    unique_articles = []
    seen_titles = set()

    for article in articles:

        title = article.get("title", "").strip()

        if not title:
            continue

        title_key = title.lower()

        if title_key in seen_titles:
            continue

        seen_titles.add(title_key)
        unique_articles.append(article)

    print("Unique Articles:", len(unique_articles))

    # SAVE ORIGINAL API RESPONSE

    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(backend_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    filepath = os.path.join(data_dir, f"{category.lower()}_news.json")

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"JSON saved successfully to {filepath}!")

    return unique_articles, len(unique_articles)