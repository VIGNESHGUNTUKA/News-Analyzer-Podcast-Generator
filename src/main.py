from textcleaner import cleaner
from frequencyanalizer import freq
from frequencyanalizer import most_freq_word
from frequencyanalizer import top_5_words
from config import stop_words
from keywordextractor import extract_keyword
from categorydetector import detect_category
from reportgenerator import generate_report
from userchoice import category_selection
from summerize import summarize
from texttospeech import generate_audio
from translator import translation

# FUNCTIONS DECLARATION
file_path,cate,language,lang_code=category_selection()

with open(file_path, "r") as file:
    data = file.read()

cleaned=cleaner(data)

words=cleaned.lower().split()

dictionary=freq(words,stop_words)

freq_word,count=most_freq_word(dictionary)

sorted_words=top_5_words(dictionary)

keyword_lis=extract_keyword(sorted_words)

winner=detect_category(keyword_lis)

summary=summarize(data,keyword_lis)

translated_summary=translation(summary,lang_code)

generate_report(
    len(words),
    len(dictionary),
    keyword_lis[:5],
    winner,freq_word,cate,
    language,
    translated_summary
)

generate_audio(translated_summary,cate,language,lang_code)

print(f"{cate} REPORT GENERATED SUCCESSFULLY!\nCHECK output/{cate}.txt FOR REPORT")

# PRINT STATEMENTS
# print("Cleaned text:",cleaned)
# print("-----------------------------------------------------------------------------------------------")
# print("Dictionary:",dictionary)
# print("-----------------------------------------------------------------------------------------------")
# print("Total Words:", len(words))
# print("-----------------------------------------------------------------------------------------------")
# print("Unique Words:", len(dictionary))
# print("-----------------------------------------------------------------------------------------------")
# print("Most frequency word:",freq_word)
# print("-----------------------------------------------------------------------------------------------")
# print(sorted_words)
# print("-----------------------------------------------------------------------------------------------")
# print(keyword_lis)
# print("-----------------------------------------------------------------------------------------------")
# print(winner)
# print("-----------------------------------------------------------------------------------------------")
# print(translated_summary)