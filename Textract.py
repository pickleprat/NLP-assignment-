import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

def getURLTitle(url):
    try:
        webpage = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}).text
        soup = BeautifulSoup(webpage, 'lxml')
        return soup.find('h1', class_='entry-title').text
    except Exception as e:
        return ''

def getURLContent(url):
    try:
        webpage = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}).text
        soup = BeautifulSoup(webpage, 'lxml')
        return soup.find('div', class_='td-post-content').text.replace('/n', ' ')
    except Exception as e: 
        return ''

def makeBlogData():
    urls = pd.read_excel('Data/Input.xlsx', index_col='URL_ID')
    urls['TITLE'] = urls.URL.apply(getURLTitle)
    urls['CONTENT'] = urls.URL.apply(getURLContent)
    urls.to_excel('Data/bloginfo.xlsx')



makeBlogData()

    
            


    

    





   
    
    
    


    