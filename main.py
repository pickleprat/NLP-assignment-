import CleanBlog 
import ScoreWords  
import SentenceProperties 
import pandas as pd 
import numpy as np 

if __name__ == '__main__':
    output = pd.read_csv('Output Data.csv')
    Input = pd.read_excel('Data/Input.xlsx')
    df = pd.merge(left=Input, right=output, on='URL').drop(['CLEANED', 'UNCLEANED'], axis=1)
    df['URL_ID'] = np.int32(df.URL_ID) 
    df.to_csv('Output Data.csv', index=False)
    print('CSV READY !!!')



