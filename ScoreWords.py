import pandas as pd 
import numpy as np 

def getSubjectivity(p, n, text):
    try:
        words = len(text.split(' ')) 
    except Exception as e: 
          return np.nan

    return (p + n)/(words + 0.0000001) 



def getPositiveScore(text, positive_words):
    try:
        words = text.lower().split(' ')
    except Exception as e:
        words = ['']

    score = 0 
    if len(words) == 1: return np.nan
    for word in words: 
        if word.lower() in positive_words:
            score += 1
    return score 

def getNegativeScore(text, negative_words):
    try:
        words = text.lower().split(' ')
    except Exception as e:
        words = ['NULL']
    if len(words) == 1: return np.nan
    score = 0 
    for word in words: 
        if word.lower() in negative_words:
            score -= 1
    return -1*score 
    
def getPolarity(p, n):
    return (p - n)/(p + n + 0.0000001)


def getSentimentalWords():
    with open('SubstituteFiles/negative-words.txt', 'r') as neg:
        negatives = neg.read().lower().split('\n')

    with open('SubstituteFiles/positive-words.txt', 'r') as pos:
        positives = pos.read().lower().split('\n')

    return negatives, positives 



# Main Code 
negative_words, positive_words = getSentimentalWords()

blog = pd.read_csv('Data/blogcleaned.csv')
uncleaned_blog = pd.read_excel('Data/blogdata.xlsx')
df = pd.merge(left = blog, right=uncleaned_blog, on='URL')
df = df.rename({"text_x":"CLEANED", "text_y":"UNCLEANED"}, axis=1)
df.to_csv('Data/merged.csv', index=False)

blog = pd.read_csv('Data/merged.csv').drop(['Unnamed: 0'], axis=1)
blog['POSITIVE_SCORE'] = blog.apply(lambda x: getPositiveScore(x.CLEANED, positive_words), axis=1)
blog['NEGATIVE_SCORE'] = blog.apply(lambda x: getNegativeScore(x.CLEANED, negative_words), axis=1)
blog['POLARITY_SCORE'] = blog.apply(lambda x: getPolarity(x.POSITIVE_SCORE, x.NEGATIVE_SCORE), axis=1)
blog['SUBJECTIVITY_SCORE'] = blog.apply(lambda x: getSubjectivity(x.POSITIVE_SCORE, x.NEGATIVE_SCORE, x.CLEANED), axis=1)


# blog['WORD_COUNT'] = blog.UNCLEANED.apply(lambda x: wordcount(x.UNCLEANED))
blog.to_csv('Data/blog.csv', index=False)
print('DATA SCORES SUBMITTED...')


