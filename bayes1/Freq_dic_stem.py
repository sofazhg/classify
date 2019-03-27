#! /usr/bin/python3
# encoding: utf-8
"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: Frequent_dic_stem.py
@time: 2019-03-14 22:20
"""

import nltk
import sys
import os
import numpy
import string
import time
from string import punctuation
from string import digits
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer

start = time.process_time()

trainfile = open(r'E:\classify\eng.txt','r')
content = trainfile.read()
filter1 = str.maketrans('', '', punctuation)  #remove punctuation in file
filter2 = str.maketrans('', '', digits)  #remove numbers in file
content = content.translate(filter1)
content = content.translate(filter2)
content = content.lower()

words = nltk.word_tokenize(content)  #tokenize the words in trainfile
print("Tokenization finished! Number of words in trainflie:")
print(len(words))

stem_words = []
for word in words:
    temp = nltk.LancasterStemmer().stem(word)  #stem the words in trainfile
    stem_words.append(temp)
print("Stemming finished! ")

freq_dist_stem = nltk.FreqDist(stem_words)  #get frequency of word stems
print(freq_dist_stem)
print("Number of total word_stems:")
print(freq_dist_stem.N())
print("Number of different word_stems:")
print(freq_dist_stem.B())

Freq_dic_stem = open('E:\classify\plan1\Freq_dic_stem.txt', mode='w', encoding='utf-8')
num_word_stems = len(freq_dist_stem.values())
for i in range(num_word_stems):
    temp = [list(freq_dist_stem.keys())[i], list(freq_dist_stem.values())[i]/freq_dist_stem.N()]  #keys()different words, values()corresponding frequencies
    Freq_dic_stem.write(str(temp)+'\n')
Freq_dic_stem.close()

end = time.process_time()
print("Program processing time：")
print(str(end - start))