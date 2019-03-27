#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 21:33
# @Author  : Zhang Shaohua
# @Site    : sofazhg@outlook.com
# @File    : get_bigrams.py
# @Software: PyCharm

import nltk
import time
import math

start = time.process_time()


def list_1mer():  #1-mer: alphabet from a to z
    return [chr(i) for i in range(ord('a'), ord('z')+1)]


def dict_2mer(l_1mer):  #26*26 2-mers from aa,ab,ac ... to ... zx,zy,zz
    l_2mer = []
    for i in l_1mer:
        for j in l_1mer:
            l_2mer.append(i+j)
    return l_2mer


def getkmer(s: str, k: int):
    result = ''
    for i in range(len(s)-k+1):
        result = result + s[i: i+k]+' '
    return result


all_sent = ''
word_train = open(r'./temp/word_train.txt', mode='r', encoding='utf-8')
for line in word_train.readlines():
    sent = getkmer(line.strip(), 2)
    all_sent = all_sent + sent

all_token = nltk.word_tokenize(all_sent)
bigram_kmer = nltk.bigrams(all_token)
#print(all_token)
#print(list(bigram_kmer))
cfd = nltk.ConditionalFreqDist(bigram_kmer)
print(len(cfd.conditions()))#fd = cfd['ny']
l_1mer =list_1mer()
l_2mer = dict_2mer(l_1mer)
mers = []
for mer in l_2mer:
    if mer not in cfd.conditions():
        mers.append(mer)
print(mers)
print(len(mers))

#fd.plot(10)
classfile = open(r'./input/tokens.txt', mode='r', encoding='utf-8')
scorefile = open(r'./output/scores.txt', mode='w', encoding='utf-8')
for line in classfile.readlines():
    kmer_string = nltk.word_tokenize(getkmer(line.strip(), 2))
    score = 1
    for i in range(len(kmer_string)-1):
        a = kmer_string[i]
        b = kmer_string[i+1]
        score = score*cfd[a][b]/len(cfd.conditions())
    if score == 0:
        score_new = 0
    else:
        score_new = -math.log(score, 10)
    scorefile.write(line.strip()+'\t'+str(score_new)+'\n')

word_train.close()
classfile.close()
scorefile.close()

end = time.process_time()
print("Program running time:")
print(str(end - start))
