import pandas as pd 
import numpy as np 
import nltk.tokenize as tk 
import syllables as syl
import re 
from nltk.corpus import stopwords 


def pronounCount(text):
    if type(text) != str: return np.nan 
    return len(re.findall('I|we|you|us|me|my|My|We|You|YOU|ME|Me|MY|WE', text)) 
    
def avgSentLen(text):
    if type(text) != str: return np.nan 
    sents = tk.sent_tokenize(text)
    sent_len = 0
    for sent in sents:
        sent_len += len(sent)
    
    return sent_len/len(sents)

def wordcount(text):
    if type(text) != str: return np.nan
    text = re.sub(r'[^\w\s]', '', text)
    for word in stopwords.words('english'):
        text = re.sub(word, '', text.lower())

    return len(tk.word_tokenize(text)) 

    
def syllableCount(text):
    if type(text) != str: return np.nan 
    words = tk.word_tokenize(text)
    count = 0
    for word in words: 
        syllables = syl.estimate(word)
        if word.lower().endswith('es') or word.lower().endswith('ed'):
            syllables -= 1 

        count += syllables 

    return count/len(words)
        
def complexWordCount(text):
    if type(text) == str:
        words = tk.word_tokenize(text)
        count = 0
        for word in words: 
            
            syllables = syl.estimate(word)
            if word.lower().endswith('es') or word.lower().endswith('ed'):
                syllables -= 1 

            if syllables > 2:
                count += 1 
            
        return count

    else: return np.nan 

def pctOfComplexWords(text, complex_count):
    if type(text) == str:
        word_count = len(tk.word_tokenize(text))
        return complex_count/word_count
    else: return np.nan 

def fogIndex(avg_sent, pctc):
    return 0.4*(avg_sent+pctc) 

def avgWordsPerSent(text):
    if type(text) == str:
        return len(tk.word_tokenize(text))/len(tk.sent_tokenize(text))
    else: return np.nan

def avgWordLen(text):
    if type(text) != str: return np.nan 
    words = tk.word_tokenize(text)
    word_len = 0
    for word in words: 
        word_len += len(word) 
    
    return word_len/len(words)

def getUpdates(dataset):
    print("Blog information \n")
    print(dataset.info())
    print("Blog description \n")
    print(dataset.describe())


# Main Code 

blog = pd.read_csv('Data/blog.csv')

blog['AVG_WORDS_PER_SENT'] = blog.UNCLEANED.apply(avgWordsPerSent)
blog['COMPLEX_WORD_COUNT'] = blog.UNCLEANED.apply(complexWordCount)
blog['PERCENT_COMPLEX'] = blog.apply(lambda x: pctOfComplexWords(x.UNCLEANED, x.COMPLEX_WORD_COUNT), axis=1)
blog['AVG_SENT_LEN'] = blog.UNCLEANED.apply(avgSentLen)
blog['FOG_INDEX'] = blog.apply(lambda x: fogIndex(x.AVG_SENT_LEN, x.PERCENT_COMPLEX), axis=1)
blog['SYLLABLE_COUNT'] = blog.UNCLEANED.apply(syllableCount)
blog['WORD_LENGTH'] = blog.UNCLEANED.apply(avgWordLen)
blog['PERSONAL_PRONOUN_COUNT'] = blog.UNCLEANED.apply(pronounCount)
blog['WORD_COUNT'] = blog.UNCLEANED.apply(wordcount)

blog.to_csv('Output Data.csv', index=False)
print('SENTENCE PROPERTIES ADDED...')

