"""
Function: word cloud from qq
Coding: utf-8
Author: Sun Yuexin
Date:
"""

import jieba  # for split Chinese
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open(r'C:\Users\fox\Documents\yu.txt', encoding='utf-8')  # open source chat text file

text_clean = open(r'C:\Users\fox\Documents\text_clean.txt', 'w', encoding="utf-8-sig")  # filter the file
str_s = text.readlines()
for s in str_s:
    if s.find('[表情]') != -1:
        s = s.replace('[表情]', '')
    elif s.find('我') != -1 or s.find('2020') != -1 or s == '' or s.find('[图片]') != -1 or s.find('的') != -1\
            or s.find('你') != -1 or s.find('是') != -1 or s.find('不') != -1 or s.find('了') != -1 \
            or s.find('吧') != -1 or s.find('就') != -1 or s.find('那') != -1 or s.find('啊') != -1 \
            or s.find('哈') != -1 or s.find('有') != -1 or s.find('在') != -1 or s.find('对') != -1 \
            or s.find('好') != -1 or s.find('嗯') != -1 or s.find('吗') != -1 or s.find('嗯') != -1 \
            or s.find('呢') != -1 or s.find('啥') != -1 or s.find('没') != -1 or s.find('可以') != -1 \
            or s.find('怎么') != -1 or s.find('一下') != -1 or s.find('嘛') != -1:
        continue
    else:
        text_clean.write(s)
text_clean.close()

text_clean = open(r'C:\Users\fox\Documents\text_clean.txt', 'r', encoding="utf-8-sig").read()  # spilt Chinese
text_jieba = jieba.cut(text_clean, cut_all=False)
text_split = " ".join(text_jieba)
print(text_split)

cloud_mask = np.array(Image.open(r'C:\Users\fox\Pictures\back.jpg'))  # set background and shape
font = r'C:\Windows\Fonts\msyh.ttc'

# 步骤六：生成词云
'''
scale : 			按比例放大画布 
background_color :	背景颜色
font_path :			字体
width :				宽
height :			高	
mask : 				nd-array or None类型 通常用于添加图片背景
max_words : 		要显示的词的最大个数
更多参数可以去看官方文档
'''
wordcloud = WordCloud(scale=10, background_color='white', width=300, height=200, font_path=font, mask=cloud_mask,
                      max_words=200).generate(text_split)
# interpolation='bilinear',排线方式
plt.imshow(wordcloud, interpolation='bilinear')
# 取消显示轴线
plt.axis('off')
# 显示图片
plt.show()
