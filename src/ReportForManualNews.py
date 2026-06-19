from datetime import datetime
def generate_report_for_manual(total, unique, top, category, freq, language,transulated_summary):
    timestamp=datetime.now().strftime("%d%m%Y_%H%M%S")
    
    with open(f"output/Report/{category}NewsReport_{language}.txt", "w", encoding="utf-8") as file:
        file.write("NEWS ANALYSER REPORT\n")
        file.write("================================================\n\n")

        file.write(f"CATEGORY:\n{",".join(category)}\n")

        file.write(f"\nTOP KEYWORDS:\n")
        
        for i , word in enumerate(top,start=1):
            file.write(f"{i}. {word}\n")

        file.write(
            f"\nSTATISTICS:\n"
            f"TOTAL WORDS: {total}\n"
            f"UNIQUE WORDS: {unique}\n"
        )

        file.write(f"\nMOST FREQUENT WORD:\n{freq}\n")

        file.write(f"\nSUMMARY:\n{transulated_summary}\n")

        file.write("\nPODCAST FILE:\n")
        file.write(f"{category}Podcast.mp3\n")

        file.write("\n================================================\n")
        file.write("Report Generated Successfully")