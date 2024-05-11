from snownlp import SnowNLP
import pandas as pd
import os

def sentiment(text):
    blob = SnowNLP(text)
    sentiment = blob.sentiments
    return sentiment

path = "./差中评未分句"
files = os.listdir(path)
for xmlFile in files: 
    full_path = os.path.join(path, xmlFile)
    reviews = pd.read_csv(full_path)
    reviews = reviews[['content']]
    reviews['sentiment'] = reviews['content'].apply(sentiment)
    reviews.to_csv("./差中评情感/" + xmlFile, index=False, sep=',')
    # 计算正面情感比例
    positive_count = len([s for s in reviews['sentiment'] if s > 0.4])
    positive_ratio = positive_count / len(reviews['sentiment'])
    # 计算中性情感比例
    neutral_count  = len([s for s in reviews['sentiment'] if (s > 0.2 and s <= 0.4)])
    neutral_ratio  = neutral_count / len(reviews['sentiment'])
    # 计算负面情感比例
    negative_count = len([s for s in reviews['sentiment'] if s <= 0.2])
    negative_ratio = negative_count / len(reviews['sentiment'])
    # 打印结果
    print(xmlFile+" 情感分析比例：")
    print("高度负面 ratio:", negative_ratio)
    print("中度负面 ratio:", neutral_ratio)
    print("一般负面 ratio:", positive_ratio)