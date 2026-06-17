def category_selection():
    user_name=input("ENTER YOUR NAME: ").upper()
    while True:
        choice=int(input(f"HELLO {user_name} SELECT THE NEWS CATEGORY:\n1.SPORTS\n2.HEALTH\n3.TECHNOLOGY\n4.MIXED\n"))
        match choice:
            case 1:
                file_name = "data/sports.txt"
                category = "Sports"
            case 2:
                file_name = "data/health.txt"
                category = "Health"
            case 3:
                file_name = "data/technology.txt"
                category = "Technology"
            case 4:
                file_name = "data/mixed.txt"
                category = "Mixed"
            case _:
                print("Invalid Choice. Try Again.")
                continue
        break
    while True:
        lan=int(input("SELECT THE LANGUAGE:\n1.ENGLISH\n2.TELUGU\n3.HINDI\n"))
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
            case _:
                print("Invalid Choice. Try Again.")
        break
    return file_name,category,language,lang_code


