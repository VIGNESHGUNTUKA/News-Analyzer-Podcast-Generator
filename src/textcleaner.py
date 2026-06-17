def cleaner(data):
    text=""
    for ch in data:
        if(ch.isalpha()):
            text+=ch
        else:
            text+=" "
    return text