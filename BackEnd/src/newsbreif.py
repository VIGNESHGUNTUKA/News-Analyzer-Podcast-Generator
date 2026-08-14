from config import connectors
def articles_to_text(articles,category,total):
    full_text=f"Welcome to today's {category} Podcast.\n\n"

    count=0
    for article in articles:
        title=article.get("title") or ""
        title=title.split(" - ")[0]
        description=article.get("description") or ""

        # Skip bad or useless descriptions
        if description in ["False", "", "null"]:
            continue

        if count==0:
            connector = "First, "
        elif count==total-1:
            connector = "Finally, "
        else:
            connector=connectors[count%len(connectors)]+" "

        full_text+=connector+title+"\n"
        full_text+=description+"\n\n"

        count+=1
        
        if count==total:
            break
    full_text+="\n\nThank you for listening. Stay tuned for more updates."

    return full_text