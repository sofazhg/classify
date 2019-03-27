#! /usr/bin/python3
# encoding: utf-8

"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: getkmer_train.py
@time: 2019-03-17 15:20
"""

import nltk
import sys
import os
import numpy
import string
import time
import random

start = time.process_time()

word_train = open(r'./temp/word_train.txt', mode='r', encoding='utf-8')
pinyin_train = open(r'./temp/pinyin_train.txt', mode='r', encoding='utf-8')
kmer_train = open(r'./temp/train_kmer.csv', mode='w', encoding='utf-8')  #textblob can directly take csv files as input
kmer_test = open(r'./temp/test_kmer.csv', mode='w', encoding='utf-8')


def getrandom(total: int, n: int):  #get n different random numbers from total numbers
    list_total = []
    for i in range(total):
        list_total.append(i)
    list_random = random.sample(list_total, n)
    return list_random


def getkmer(s: str, k: int):
    result = ''
    for i in range(len(s)-k+1):
        result = result + s[i: i+k]+' '
    return result



k_word = 2
content_word = word_train.readlines()
word_random = getrandom(len(content_word), int(0.25*len(content_word)))  #take 0.25 of total words as train set
for i in range(len(content_word)):
    if i in word_random:
        kmer_test.write(getkmer(content_word[i].strip(), k_word) + ',word\n')  #add word label to 2-mers
    else:
        kmer_train.write(getkmer(content_word[i].strip(), k_word) + ',word\n')

k_pinyin = 2
content_pinyin = pinyin_train.readlines()
pinyin_random = getrandom(len(content_pinyin), int(0.25*len(content_pinyin)))  #take 0.25 of pinyin words as train set
for j in range(len(content_pinyin)):
    if j in pinyin_random:
        kmer_test.write(getkmer(content_pinyin[j].strip(), k_pinyin) + ',pinyin\n')  #add pinyin label to 2-mers
    else:
        kmer_train.write(getkmer(content_pinyin[j].strip(), k_pinyin) + ',pinyin\n')

word_train.close()
pinyin_train.close()
kmer_test.close()
kmer_train.close()


end = time.process_time()
print("Program running time:")
print(str(end - start))
