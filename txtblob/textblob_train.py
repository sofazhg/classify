#! /usr/bin/python3
# encoding: utf-8

"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: textblob_train.py
@time: 2019-03-17 15:20
"""

import time
import os
import textblob
from textblob.classifiers import NaiveBayesClassifier

start = time.process_time()

with open(r'./temp/train_kmer.csv', mode='r', encoding='utf-8') as train_kmer:  #load train_kmer.csv as train set
    clsf = NaiveBayesClassifier(train_kmer)  #train naive Bayes classifier with train set

print('Training finished! Time consumption:')
mid = time.process_time()
print(str(mid - start))

with open(r'./temp/test_kmer.csv', mode='r', encoding='utf-8') as test_kmer:  #load test_kmer.csv as test set
    print('Classification accuracy:')
    print(clsf.accuracy(test_kmer))  #print accuracy performed on test set


def getkmer(s: str, k: int):
    result = ''
    for i in range(len(s)-k):
        result = result + s[i: i+k]+' '
    return result


classifile = open(r'./input/tokens.txt', mode='r', encoding='utf-8')
pinyin = open(r'./output/pinyin.txt', mode='w', encoding='utf-8')
words = open(r'./output/words.txt', mode='w', encoding='utf-8')

for line in classifile.readlines():  #classify words and pinyin according to predicted label
    if clsf.classify(getkmer(line, 2)) == 'word':
        words.write(line.strip() + '\n')
    if clsf.classify(getkmer(line, 2)) == 'pinyin':
        pinyin.write(line.strip() + '\n')

classifile.close()
pinyin.close()
words.close()

print('Classifying time:')
end = time.process_time()
print(str(end - mid))
