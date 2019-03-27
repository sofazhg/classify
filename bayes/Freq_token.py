#! /usr/bin/python3
# encoding: utf-8
"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: Freq_token.py
@time: 2019-03-14 22:20
"""

import nltk
import sys
import os
import string
import time
from string import punctuation
from string import digits
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer

start = time.process_time()
trainfile = open(r'./input/eng.txt', mode='r', encoding='utf-8')
content = trainfile.read()
filter1 = str.maketrans('', '', punctuation)  #remove punctuation in file
filter2 = str.maketrans('', '', digits)  #remove numbers in file
content = content.translate(filter1)
content = content.translate(filter2)
content = content.lower()

words = nltk.word_tokenize(content)  #tokenize the words in trainfile
print("Number of words in trainflie:")
print(len(words))

stem_words = []
for word in words:
    temp = nltk.LancasterStemmer().stem(word)  #stem the words in trainfile
    stem_words.append(temp)

freq_dist = nltk.FreqDist(stem_words)  #get frequency of word stems
print(freq_dist)
print("Number of total word_stems:")
print(freq_dist.N())
print("Number of different word_stems:")
print(freq_dist.B())

classifile = open(r'./input/tokens.txt', mode='r', encoding='utf-8')
terms = classifile.readlines()
tokens =[]
for term in terms:
    term.strip()
    tokens.append(term)
num_tokens = len(tokens)
print("Number of words in tokenfile：")
print(num_tokens)

num_stems = len(freq_dist.values())
freq_list = []
for j in range(num_tokens):
    freq = 0
    for i in range(num_stems):
        if list(freq_dist.keys())[i] in tokens[j]:
            freq = freq + list(freq_dist.values())[i] / freq_dist.N()  #calculate the frequency of stems in string
    temp = [tokens[j], freq]
    freq_list.append(temp)


def takesecond(elem):
    return elem[1]


Freq_token = open(r'./output/Freq_token.txt', mode='w', encoding='utf-8')
freq_list.sort(key=takesecond)  #sort freq_list according to frequency
for sort_token in freq_list:
    Freq_token.write(str(sort_token)+'\n')  #write freq_list to txt file
Freq_token.close()

end = time.process_time()
print('Program processing time：')
print(str(end - start))
