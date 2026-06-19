def category_selection(name):
    while True:
        choice=int(input(f"HELLO {name} SELECT THE NEWS CATEGORY:\n1.SPORTS\n2.HEALTH\n3.TECHNOLOGY\n4.General\n"))
        match choice:
            case 1:
                category = "Sports"
            case 2:
                category = "Health"
            case 3:
                category = "Technology"
            case 4:
                category = "General"
            case _:
                print("Invalid Choice. Try Again.")
                continue
        break
    return category

def language_selection():
    while True:
        lan=int(input("SELECT THE LANGUAGE:\n1.ENGLISH\n2.TELUGU\n3.HINDI\n4.TAMIL\n"))
        match lan:
            case 1:
                language="English"
                lang_code="en"
            case 2:
                language="Telugu"
                lang_code="te"
            case 3:
                language="Hindi"
                lang_code="hi"
            case 4:
                language="Tamil"
                lang_code="ta"
            case _:
                print("Invalid Choice. Try Again.")
                continue
        break
    return language,lang_code


