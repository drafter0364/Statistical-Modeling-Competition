import pandas as pd
import re
import opencc
import numpy as np
# 去重，去除完全重复的数据
reviews = pd.read_csv("./马铃薯评论1.csv")
reviews = reviews[['content']].drop_duplicates()

# 用空字符串('')替换纯数字('123')
def remove_alldigit(desstr,restr=''):  
    digit_pattern = re.compile('^[0-9]*$')
    return digit_pattern.sub(restr, desstr)
reviews['content'] = reviews['content'].apply(remove_alldigit)

# 用空字符串('')替换('111','aaa')等
def remove_continuousdigit(desstr,restr=''):
    digit_pattern = re.compile(r'^(.)\1+$')
    return digit_pattern.sub(restr, desstr)
reviews['content'] = reviews['content'].apply(remove_continuousdigit)

# 定义去除emoji的函数
def remove_emojis(desstr,restr=''):  
    try:  
        co = re.compile(u'['u'\U0001F300-\U0001F64F' u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55]+')  
    except re.error:  
        co = re.compile(u'('u'\ud83c[\udf00-\udfff]|'u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'u'[\u2600-\u2B55])+')  
    return co.sub(restr, desstr)
def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)
# 去除表情符号
reviews['content'] = reviews['content'].apply(remove_emojis)
reviews['content'] = reviews['content'].apply(filter_emoji)

# 创建一个OpenCC实例，指定繁简转换规则为"t2s.json"
converter = opencc.OpenCC('t2s.json')
# 繁体转简体
reviews['content'] = reviews['content'].apply(converter.convert)

# 将空字符串转为'np.nan',即NAN,用于下一步删除这些评论
reviews.replace(to_replace=r'^\s*$', value=np.nan, regex=True, inplace=True)
# 删除comment中的空值，并重置索引
reviews = reviews.dropna(subset=['content'])
reviews.reset_index(drop=True, inplace=True)
content = reviews['content']
print(content)
reviews.to_csv("马铃薯1.csv",index=False,sep=',')