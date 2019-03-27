#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 10:23
# @Author  : Zhang Shaohua
# @Contact    : sofazhg@outlook.com
# @File    : analyse_kmer.py
# @Software: PyCharm

import nltk
import time
import math
from string import punctuation
from string import digits

start = time.process_time()


def getkmer(s: str, k: int):
    result = ''
    for i in range(len(s)-k+1):
        result = result + s[i: i+k] + ' '
    return result


trainfile = open(r'./input/eng.txt', mode='r', encoding='utf-8')
content = trainfile.read()
filter1 = str.maketrans('', '', punctuation)  #remove punctuation in eng.txt
filter2 = str.maketrans('', '', digits)  #remove numbers in eng.txt
content = content.translate(filter1)
content = content.translate(filter2)
content = content.lower()
trainfile.close()
words = nltk.word_tokenize(content)  #tokenize eng.txt with nltk
print("Tokenization finished! Number of words in trainflie:")
print(len(words))

list_2mer = ''
list_3mer = ''
for word in words:
    if len(word) >= 2:
        list_2mer = list_2mer + getkmer(word, 2)  #get 2mer list of words in eng.txt
    if len(word) >= 3:
        list_3mer = list_3mer + getkmer(word, 3)  #get 3mer list of words in eng.txt

freq_dist_2mer = nltk.FreqDist(nltk.word_tokenize(list_2mer))  #get the frequency dictionary of 2mers
print(freq_dist_2mer)
print("Number of total 2mers:")
print(freq_dist_2mer.N())
print("Number of different 2mers:")
print(freq_dist_2mer.B())

freq_dist_3mer = nltk.FreqDist(nltk.word_tokenize(list_3mer))  #get the frequency dictionary of 3mers
print(freq_dist_3mer)
print("Number of total 3mers:")
print(freq_dist_3mer.N())
print("Number of different 3mers:")
print(freq_dist_3mer.B())

"""
#These codes are used to find rare3mers that eng.txt might not cover.
#Pinyins tend to contain more than one rare3mer.
#Thus, if there is only one rare3mer in a string in tokens.txt, the string is likely to be a word rather than a pinyin.
#Then this rare3mer should be added into the freq_dist_3mer dictionary in order not to filter the corresponding word.
classfile = open(r'./input/tokens.txt', mode='r', encoding='utf-8')
rarekmer = []
for line in classfile.readlines():
    line = line.strip()
    if len(line) >= 3:
        line_3mer = nltk.word_tokenize(getkmer(line, 3))
        temp = []
        for mer3 in line_3mer:
            if freq_dist_3mer[str(mer3)] == 0:
                temp.append(mer3)  #find rare3mers in strings in tokens.txt
        if len(temp) == 1:
            rarekmer.append(temp[0])  #if only one rare3mer, add this rare3mer to freq_dist_3mer

rarekmer_dic = nltk.FreqDist(rarekmer)
print(rarekmer_dic)
freq_dist_3mer.update(rarekmer_dic)
print(freq_dist_3mer)
classfile.close()
"""

classfile_new = open(r'./input/tokens.txt', mode='r', encoding='utf-8')
#scorefile = open(r'./output/scores_new.txt', mode='w', encoding='utf-8')
words = open(r'./output/words.txt', mode='w', encoding='utf-8')
pinyin = open(r'./output/pinyin.txt', mode='w', encoding='utf-8')
filter3 = str.maketrans('', '', '-')  #remove '-' in strings in tokens.txt
for line1 in classfile_new.readlines():
    line1 = line1.strip()
    temp = line1.translate(filter3)
    if len(temp) >= 3:  #if string is longer than 3 letters, cut it into 3mers
        line_3mer = nltk.word_tokenize(getkmer(temp, 3))
        score = 1
        for mer3 in line_3mer:  #calculate their score with frequency dictionary of 3mers
            score = score * (freq_dist_3mer[str(mer3)] / freq_dist_3mer.N())
    else:  #if string is shorter than 3 letters, calculate their score with frequency dictionary of 2mers
        score = freq_dist_2mer[str(line1)]/freq_dist_2mer.N()
    if score == 0:
        pinyin.write(line1 + '\n')
        #score_new = 0
    else:
        words.write(line1 + '\n')
        #score_new = -math.log(score, 10)  #transfer the score from small number to big number
    #scorefile.write(line1 + '\t' + str(score_new) +'\n')  #write strings and their scores into scores_new.txt

classfile_new.close()
#scorefile.close()
words.close()
pinyin.close()

end = time.process_time()
print("Program running time:")
print(str(end - start))



