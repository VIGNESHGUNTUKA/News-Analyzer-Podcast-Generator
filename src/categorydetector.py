from config import category
from frequencyanalizer import most_freq_word

def detect_category(keyword_lis):
    score_dic = {
    "Sports": 0,
    "Health": 0,
    "Technology": 0,
    "Politics": 0,
    "Business": 0,
    "Entertainment": 0
    }
    # FINDING THE SCORE OF EACH CATEGORY
    for word in keyword_lis:
        for cate,words in category.items():
            if word in words:
                score_dic[cate]+=1

    # CHECKING FOR WINNER FROM THE SCORE DICTIONARY 
    freq,score=most_freq_word(score_dic)
    if score==0:
        return []
    else:
        winner=[]
        for cate,count in score_dic.items():
            if count==score:
                winner.append(cate)
    return winner


                        
