def summarize(text, keyword_lis):

    # SPLIT INTO SENTENCES
    sentences = text.split(".")

    sentence_score = {}

    # SCORE EACH SENTENCE
    for index, sentence in enumerate(sentences):

        sentence = sentence.strip()

        if sentence == "":
            continue

        count = 0

        for word in keyword_lis:
            if word in sentence.lower():
                count += 1

        sentence_score[sentence] = (count, index)

    # SORT BY SCORE
    sorted_sent = sorted(
        sentence_score.items(),
        key=lambda item: item[1][0],
        reverse=True
    )

    # TAKE TOP 3 SENTENCES
    top_sentence = sorted_sent[:3]

    # RESTORE ORIGINAL ORDER
    top_sentence = sorted(
        top_sentence,
        key=lambda item: item[1][1]
    )

    # ALWAYS INCLUDE FIRST SENTENCE
    summary = []

    first_sentence = sentences[0].strip()

    if first_sentence:
        summary.append(first_sentence)

    # ADD TOP SENTENCES WITHOUT DUPLICATES
    for sentence, (count, index) in top_sentence:

        if sentence not in summary:
            summary.append(sentence)

        if len(summary) == 3:
            break

    # BUILD FINAL SUMMARY STRING
    final_summary = ""

    for sentence in summary:
        final_summary += sentence + ".\n"

    return final_summary