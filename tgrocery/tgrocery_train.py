#! /usr/bin/python3
# encoding: utf-8

"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: tgrocery_train.py
@time: 2019-03-17 15:20
"""

import time
import os
import tgrocery
from tgrocery import Grocery

start = time.process_time()

word_train = open(r'E:\classify\plan2\word_train.txt', mode='r', encoding='utf-8')
pinyin_train = open(r'E:\classify\plan2\pinyin_train.txt', mode='r', encoding='utf-8')
kmer_train = open(r'E:\classify\plan2\train_kmer.txt', mode='w', encoding='utf-8')
kmer_test = open(r'E:\classify\plan2\test_kmer.txt', mode='w', encoding='utf-8')


def getkmer(s: str, k: int):
    result = ''
    for i in range(len(s)-k):
        result = result + s[i: i+k]+' '
    return result


k_word = 2
content_word = word_train.readlines()
for i in range(int(len(content_word)/10)):
    kmer_test.write('word,' + getkmer(content_word[i], k_word) + '\n')
for i in range(int(len(content_word)/10)+1, len(content_word)):
    kmer_train.write('word,' + getkmer(content_word[i], k_word) + '\n')

k_pinyin = 2
content_pinyin = pinyin_train.readlines()
for j in range(int(len(content_pinyin)/10)):
    kmer_test.write('pinyin,' + getkmer(content_pinyin[j], k_pinyin) + '\n')
for j in range(int(len(content_pinyin)/10)+1,len(content_pinyin)):
    kmer_train.write('pinyin,' + getkmer(content_pinyin[j], k_pinyin) + '\n')

word_train.close()
pinyin_train.close()
kmer_train.close()

grocery = Grocery('sample')
train_src = r'E:\classify\plan2\train_kmer.txt'
grocery.train(train_src, delimiter=',')
print('Training finished! Time consumption:')
mid = time.process_time()
print(str(mid - start))
grocery.save()

grocery.load()
test_src = r'E:\classify\plan2\test_kmer.txt'
print('Classification accuracy:')
print(grocery.test(test_src, delimiter=','))

classifile = open(r'E:\classify\tokens.txt', mode='r', encoding='utf-8')
pinyin = open(r'E:\classify\pinyin_grocery.txt', mode='w', encoding='utf-8')
words = open(r'E:\classify\words_grocery.txt', mode='w', encoding='utf-8')

for line in classifile.readlines():
    if grocery.predict(getkmer(line, 2)) == 'word':
        words.write(line)
    if grocery.predict(getkmer(line, 2)) == 'pinyin':
        pinyin.write(line)

classifile.close()
pinyin.close()
words.close()

print('Program running time:')
end = time.process_time()
print(str(end - start))
