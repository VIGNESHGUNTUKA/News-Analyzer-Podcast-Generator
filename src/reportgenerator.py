def generate_report(total, unique, top, category, freq, selected_cate, language,transulated_summary):
    with open(f"output/{selected_cate}NewsReport_{language}.txt", "w", encoding="utf-8") as file:
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
        file.write(f"{selected_cate}Podcast.mp3\n")

        file.write("\n================================================\n")
        file.write("Report Generated Successfully")