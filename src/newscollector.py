import requests
from dotenv import load_dotenv
import os,json

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

api_key = os.getenv("NEWS_API_KEY")


def collect_news(category):

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"country=us&category={category.lower()}&apiKey={api_key}"
    )

    response = requests.get(url)

    print("Status Code:", response.status_code)

    data = response.json()

    with open(f"data/{category.lower()}_news.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("JSON saved successfully!")

    print("Status:", data["status"])
    print("Total Results:", data["totalResults"])
    print("Articles Retrieved:", len(data["articles"]))

    return data["articles"],len(data["articles"])
