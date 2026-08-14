from datetime import datetime
import edge_tts
import asyncio


def generate_audio(translated_summary, cate, language, lang_code, voice):

    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

    filename = f"output/Podcast/{cate}NewsPodcast_{language}_{timestamp}.mp3"

    communicate = edge_tts.Communicate(
        translated_summary,
        voice
    )

    asyncio.run(communicate.save(filename))

    print("Podcast generated successfully!")