#! /usr/bin/python3
# encoding: utf-8

"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: svm_search.py
@time: 2019-03-17 15:20
"""

import sklearn
import os
import sys
import time
import random
from feature_gen import list_1mer
from feature_gen import dict_2mer
from feature_gen import feature_gen

start = time.process_time()


def getrandom(total: int, n: int):  #get n different random numbers from total numbers
    list_total = []
    for i in range(total):
        list_total.append(i)
    list_random = random.sample(list_total, n)
    return list_random


def SVC_search(data_feature, data_label):  #search for the best C and gamma paramaters for SVM model
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import GridSearchCV
    from sklearn.svm import SVC
    X_train, X_test, y_train, y_test = train_test_split(data_feature, data_label, test_size=0.25)
    param_grid = {'C': [1e1, 1e2, 1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }  #train 7*6 = 42 estimators in total
    clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced', probability=True), param_grid)
    clf = clf.fit(X_train, y_train)  #fitting model
    print(clf.best_estimator_)  #print the best estimator
    print(clf.score(X_test, y_test))  #print accuracy performed on the test set


l_1mer = list_1mer()
l_2mer = dict_2mer(l_1mer)
word_train = open(r'./temp/word_train.txt', mode='r', encoding='utf-8')
pinyin_train = open(r'./temp/pinyin_train.txt', mode='r', encoding='utf-8')
Data_Feature = []
Data_Label = []

content1 = word_train.readlines()
for i in getrandom(len(content1), 2000):  #take 2000 word samples randomly for searching best paramaters
    Data_Feature.append(feature_gen(l_2mer, content1[i]))
    Data_Label.append(1)  #data_label of word is 1

content2 = pinyin_train.readlines()
for j in getrandom(len(content2), 2000):  #take 2000 pinyin samples randomly for searching best paramaters
    Data_Feature.append(feature_gen(l_2mer, content2[j]))
    Data_Label.append(0)  #data_label of word is 0

SVC_search(Data_Feature, Data_Label)  #training various estimators and searching best paramaters

print('Program running time:')
end = time.process_time()
print(str(end - start))
