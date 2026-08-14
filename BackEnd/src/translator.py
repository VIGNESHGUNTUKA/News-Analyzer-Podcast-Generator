from deep_translator import GoogleTranslator

def translation(summary,lang_code):
    if lang_code=="en":
        return summary
    translated_summary=GoogleTranslator(
        source="en",
        target=lang_code
    ).translate(summary)

    return translated_summary
