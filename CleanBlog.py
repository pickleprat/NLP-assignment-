import pandas as pd 
import os 
import numpy as np 

DIR = './StopWords'


def concat(title, content):
    return f"{title}  {content}"

def readCurrencies():
    with open('StopWords/StopWords_Currencies.txt', 'r') as f:
        text = f.read().lower().split('\n')
    currenies = []
    for words in text:
        try:
            word1 = words.split(' | ')[0]
            currenies.append(word1)
        except Exception as e: 
            continue

    return currenies


def removeStopWords(text, stopwords):
    if type(text) != str: return np.nan
    words = text.split(' ')
    content = ''
    for word in words: 
        if word.lower() not in stopwords: 
            content += word + ' ' 

    content = content.replace('\n', ' ')
    return content 
        
def collectStopWords(DIR=DIR):
    words = []
    for txt in os.listdir(DIR):
        if txt == 'StopWords_Currencies.txt': continue
        with open(f'{DIR}/{txt}', 'r') as f: 
            words += f.read().lower().split('\n')

    return words
        

# Main Code 

bloginfo = pd.read_excel('Data/bloginfo.xlsx')
bloginfo['text'] = bloginfo.apply(lambda x: concat(x.TITLE, x.CONTENT), axis=1)
bloginfo.to_excel('Data/blogdata.xlsx', index=False)

blog = pd.read_excel('Data/blogdata.xlsx')
words = collectStopWords()
currencies = readCurrencies()
stopwords = words + currencies
blog['text'] = blog.apply(lambda x: removeStopWords(x.text, stopwords), axis=1)
blog.to_csv('Data/blogcleaned.csv')
print('DATA CLEANED...')

    
    


    
    


    
        

