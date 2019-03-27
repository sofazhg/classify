#! /usr/bin/python3
# encoding: utf-8

"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: svm_classify.py
@time: 2019-03-17 15:20
"""

import sklearn
import os
import sys
import time
from sklearn.externals import joblib
from feature_gen import list_1mer
from feature_gen import dict_2mer
from feature_gen import feature_gen

start = time.process_time()

l_1mer = list_1mer()
l_2mer = dict_2mer(l_1mer)
classifile = open(r'./input/tokens.txt', mode='r', encoding='utf-8')
pinyin = open(r'./output/pinyin.txt', mode='w', encoding='utf-8')
words = open(r'./output/words.txt', mode='w', encoding='utf-8')

Data_Feature = []
clf_new = joblib.load(r'./model/clf.pkl')  #load trained SVM classifer clf.pkl as clf_new
content = classifile.readlines()
for line in content:
    Data_Feature.append(feature_gen(l_2mer, line))  #generate data_feature for tokens.txt

Data_Label = clf_new.predict(Data_Feature)  #predict strings in tokens.txt as word or pinyin
#Data_Proba = clf_new.predict_proba(Data_Feature)  #view the probabilities of prediction
for i in range(len(Data_Label)):
    if Data_Label[i] == 1:
        words.write(content[i])
        #words.write(content[i].strip() + ' ' + str(Data_Proba[i]) + '\n')  #write the probabilities of prediction into words.txt as well
    if Data_Label[i] == 0:
        pinyin.write(content[i])
        #pinyin.write(content[i].strip() + ' ' + str(Data_Proba[i]) + '\n')  #write the probabilities of prediction into pinyin.txt as well

classifile.close()
pinyin.close()
words.close()

print('Program running time:')
end = time.process_time()
print(str(end - start))
