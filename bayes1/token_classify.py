#! /usr/bin/python3
# encoding: utf-8
"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: StemExtract.py
@time: 2019-03-14 22:20
"""

import nltk
import sys
import os
import numpy as np
import string
import time
from string import punctuation
from string import digits
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer

start = time.process_time()

Freq_dic_stem = open(r'E:\classify\plan1\Freq_dic_stem.txt', mode='r', encoding='utf-8')
stems = Freq_dic_stem.readlines()
stemsDict = dict(stems)


classifile = open(r'E:\classify\tokens.txt', mode='r', encoding='utf-8')
terms = classifile.readlines()
tokens =[]
for term in terms:
    term.strip()
    tokens.append(term)
num_tokens = len(tokens)
print("Number of words in tokenfile：")
print(num_tokens)

num_stems = len(stemsDict.values())
freq_list = []
for j in range(10):
    freq = 0
    for i in range(num_stems):
        if list(stemsDict.keys())[i] in tokens[j]:
            freq = freq + list(stemsDict.values())[i]  #calculate the frequency of multiple stems in one single string
    temp = [tokens[j], freq]
    freq_list.append(temp)



def takesecond(elem):
    return elem[1]


Freq_token = open('E:\classify\plan1\Freq_token.txt', mode='w', encoding='utf-8')
freq_list.sort(key=takesecond)  #sort freq_list according to frequency
for sort_token in freq_list:
    Freq_token.write(str(sort_token)+'\n')
Freq_token.close()

end = time.process_time()
print('Program processing time：')
print(str(end - start))
