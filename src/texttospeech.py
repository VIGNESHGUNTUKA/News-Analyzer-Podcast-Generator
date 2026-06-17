from gtts import gTTS

def generate_audio(translated_summary,cate,language,lang_code):

    tts = gTTS(
        text=translated_summary,
        lang=lang_code,
        slow=False
    )

    tts.save(f"output/{cate}NewsPodcast_{language}.mp3")

    print("Podcast generated successfully!")