#! /usr/bin/python3
# encoding: utf-8

"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: getword_train.py
@time: 2019-03-14 22:20
"""

import sys
import os
import string
import nltk
import time
from string import punctuation
from string import digits

start = time.process_time()

trainfile = open(r'./input/eng.txt', mode='r', encoding='utf-8')
content = trainfile.read()
filter1 = str.maketrans('', '', punctuation)  #remove punctuation in eng.txt
filter2 = str.maketrans('', '', digits)  #remove numbers in eng.txt
content = content.translate(filter1)
content = content.translate(filter2)
content = content.lower()

words = nltk.word_tokenize(content)  #tokenize eng.txt with nltk
print("Tokenization finished! Number of words in trainflie:")
print(len(words))

freq_dist = nltk.FreqDist(words)
print(freq_dist)
print("Number of total words:")
print(freq_dist.N())
print("Number of different words:")
print(freq_dist.B())

num_words = len(freq_dist.values())
Freq_dic = open(r'./temp/word_train.txt', mode='w', encoding='utf-8')
for i in range(num_words):
    temp = list(freq_dist.keys())[i]  #keys() are different words, values() are corresponding frequencies
    Freq_dic.write(str(temp)+'\n')  #get all different words in eng.txt
Freq_dic.close()

end = time.process_time()
print("Program running time:")
print(str(end - start))

