from datetime import datetime
def generate_report_for_automatic(category,language,total_articles,translated_summary):
    timestamp=datetime.now().strftime("%d%m%Y_%H%M%S")

    with open(f"output/Report/{category}Newsreport_{language}_{timestamp}.txt","w",encoding="utf-8")as file:
        file.write("NEWS ANALYSER REPORT\n")
        file.write("================================================\n\n")

        file.write(f"CATEGORY:\n{category}\n")

        file.write(f"Language\n{language}\n")

        file.write(f"Number of articles{total_articles}\n")

        file.write(f"\nSUMMARY:\n{translated_summary}\n")

        file.write("\nPODCAST FILE:\n")
        file.write(f"{category}Podcast_{timestamp}.mp3\n")

        file.write("\n================================================\n")
        file.write("Report Generated Successfully")