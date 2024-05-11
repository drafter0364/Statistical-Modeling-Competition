import pandas as pd
import jieba
import os  
import os.path
from xml.etree.ElementTree import parse, Element
def tokenize(text):
    return jieba.lcut(text, cut_all=False)
path = "./清洗后数据"
files = os.listdir(path)
for xmlFile in files: 
    full_path = os.path.join(path, xmlFile)
    reviews = pd.read_csv(full_path)
    reviews = reviews[['content']].drop_duplicates()
    reviews['content'] = reviews['content'].apply(tokenize)
    reviews['content'] = reviews['content'].apply(lambda x: ' '.join(x))
    print(reviews)
    reviews.to_csv("./分词/分词_"+xmlFile,index=False,sep=',')