from config import STOP_WORDS
from userchoice import category_selection,language_selection
from textcleaner import cleaner
from frequencyanalizer import freq
from frequencyanalizer import most_freq_word
from frequencyanalizer import top_5_words
from keywordextractor import extract_keyword
from categorydetector import detect_category
from ReportForManualNews import generate_report_for_manual
from summerize import summarize
from translator import translation
from texttospeech import generate_audio

from newscollector import collect_news
from newsbreif import articles_to_text
from ReportForAutomaticNews import generate_report_for_automatic

user_name=input("ENTER YOUR NAME: ").upper()

mode=int(input("SELECT THE MODE:\n1.PASTE THE NEWS\n2.AUTOMATIC NEWS\n"))

if mode==1:
    print("Paste your article below.\nType END on a new line when finished.")
    data=""
    while True:
        line=input()
        if line=="END":
            break
        else:
            data+=line+"\n"
    
    cleaned=cleaner(data)

    words=cleaned.lower().split()

    dictionary=freq(words,STOP_WORDS)

    freq_word,count=most_freq_word(dictionary)

    sorted_words=top_5_words(dictionary)

    keyword_lis=extract_keyword(sorted_words)

    winner=detect_category(keyword_lis)
    category="_".join(winner)
    summary=summarize(data,keyword_lis)

    language,lang_code=language_selection()

    translated_summary=translation(summary,lang_code)

    generate_report_for_manual(
        len(words),
        len(dictionary),
        keyword_lis[:5],
        winner,freq_word,
        language,
        translated_summary
    )

    generate_audio(translated_summary,winner,language,lang_code)

    print(f"{category} REPORT GENERATED SUCCESSFULLY!\nCHECK output/{category}.txt FOR REPORT")

else:
    category=category_selection(user_name)

    language,lang_code=language_selection()

    articles,result=collect_news(category)
    if result>20:
        result=20
    else:
        result=result
    if(result!=0):
        summary=articles_to_text(articles,category,result)

        translated_summary=translation(summary,lang_code)

        generate_report_for_automatic(category,language,len(articles),translated_summary)

        generate_audio(translated_summary,category,language,lang_code)
    else:
        print("THERE IS NO ARTICLES FOR SELECTED CATEGORY")

    

        