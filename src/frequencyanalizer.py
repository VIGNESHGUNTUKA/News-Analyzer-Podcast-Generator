def freq(words,stop):
    word_freq={}
    for word in words:
        if word not in stop:
            if word in word_freq:
                word_freq[word]+=1
            else:
                word_freq[word]=1
    return word_freq

def most_freq_word(word_freq):
    max_val=0
    freq_word=""
    for key,value in word_freq.items():
        if value>max_val:
            max_val=value
            freq_word=key
    return freq_word,max_val

def top_5_words(word_freq):

    sorted_words = sorted(
        word_freq.items(),
        key=lambda item: item[1],
        reverse=True
    )
    
    # for word, count in sorted_words[:5]:
    #     print(word, "->", count)
    
    return sorted_words