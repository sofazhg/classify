#! /usr/bin/python3
# encoding = utf-8
"""
@author: Zhang Shaohua
"""

import os
words = open(r'E:\classify\plan2\word_train.txt', mode='r', encoding='utf-8')
length_words_sum = 0
for line in words.readlines():
    length_words_sum = length_words_sum + len(line)

pinyins = open(r'E:\classify\plan2\pinyin_train.txt', mode='r', encoding='utf-8')
length_pinyins_sum = 0
for line in pinyins.readlines():
    length_pinyins_sum = length_pinyins_sum + len(line)

print('Average length of words:')
print(length_words_sum/35536)
print('Average length of pinyins:')
print(length_pinyins_sum/35536)
