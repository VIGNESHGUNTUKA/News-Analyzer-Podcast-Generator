from config import CATEGORY_KEYWORDS
from frequencyanalizer import most_freq_word

def detect_category(keyword_lis):
    score_dic = {}
    for category in CATEGORY_KEYWORDS:
        score_dic[category]=0

    # FINDING THE SCORE OF EACH CATEGORY
    for word in keyword_lis:
        for cate,words in CATEGORY_KEYWORDS.items():
            if word in words:
                score_dic[cate]+=1

    # CHECKING FOR WINNER FROM THE SCORE DICTIONARY 
    freq,score=most_freq_word(score_dic)
    if score==0:
        return ["Uncategorized"]
    else:
        winner=[]
        for cate,count in score_dic.items():
            if count==score:
                winner.append(cate)
    return winner


                        
