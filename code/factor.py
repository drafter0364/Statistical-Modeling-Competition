import pandas as pd
import os
import numpy as np
# 假设你的数据框名为 reviews，列名为 'content' 和 'convenience'
# 创建一个函数来检查评论内容是否包含“方便”
def check_delicious(text):
    if '好吃' in text or '口感' in text or '口味' in text or '美味' in text or '特别' in text\
    or '味道' in text or '香' in text or '甜' in text or '浓' in text or '脆' in text or '酸甜' in text\
    or '多汁' in text or '可口' in text or '汁水' in text or '水分' in text or '筋道' in text :
        return 1
    else:
        return 0

def check_price(text):
    if '物美价廉' in text or '实惠' in text or '值得' in text or '性价比' in text or '划算' in text\
    or '便宜' in text or '价格':
        return 1
    else:
        return 0

def check_quality(text):
    if '质量' in text or '新鲜' in text or '分量' in text or '干净' in text or '饱满' in text\
    or '很足' in text or '均匀' in text or '个头' in text or '大小' in text or '品质' in text or '真的' in text\
    or '份量' in text or '保鲜' in text or '嫩' in text:
        return 1
    else:
        return 0

def check_logistics(text):
    if '方便' in text or '很快' in text or '包装' in text or '完整' in text or '物流' in text\
    or '速度' in text or '严实' in text:
        return 1
    else:
        return 0

def check_convinience(text):
    if '方便' in text:
        return 1
    else:
        return 0

def check_service(text):
    if '服务态度' in text or '商家' in text or '卖家' in text or '客服' in text:
        return 1
    else:
        return 0
path = "./好评情感"
files = os.listdir(path)
for xmlFile in files: 
    full_path = os.path.join(path, xmlFile)
    reviews = pd.read_csv(full_path)
    # 应用函数到 'content' 列，将结果赋值给 'convenience' 列
    print(reviews)
    reviews['sentiment'] = np.ceil(reviews['sentiment'] * 4 + 1)
    reviews['taste'] = reviews['content'].copy().apply(check_delicious) * reviews['sentiment']
    reviews['price'] = reviews['content'].copy().apply(check_price) * reviews['sentiment']
    reviews['quality'] = reviews['content'].copy().apply(check_quality) * reviews['sentiment']
    reviews['logistics'] = reviews['content'].copy().apply(check_logistics) * reviews['sentiment']
    reviews['convinience'] = reviews['content'].copy().apply(check_convinience) * reviews['sentiment']
    reviews['service'] = reviews['content'].copy().apply(check_service) * reviews['sentiment']
    reviews.drop(columns=['content'], inplace=True)
    print(reviews)
    reviews.to_csv("./好评因素/" + xmlFile, index=False, sep=',')