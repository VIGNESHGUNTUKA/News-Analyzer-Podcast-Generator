from datetime import datetime
from gtts import gTTS

def generate_audio(translated_summary,cate,language,lang_code):
    timestamp=datetime.now().strftime("%d%m%Y_%H%M%S")
    tts = gTTS(
        text=translated_summary,
        lang=lang_code,
        slow=False
    )

    tts.save(f"output/Podcast/{cate}NewsPodcast_{language}_{timestamp}.mp3")

    print("Podcast generated successfully!")