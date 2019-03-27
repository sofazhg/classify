#! /usr/bin/python3
# encoding: utf-8

"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: feature_gen.py
@time: 2019-03-17 15:20
"""


def list_1mer():  #1-mer: alphabet from a to z
    return [chr(i) for i in range(ord('a'), ord('z')+1)]


def dict_2mer(l_1mer):  #26*26 2-mers from aa,ab,ac ... to ... zx,zy,zz
    l_2mer = []
    for i in l_1mer:
        for j in l_1mer:
            l_2mer.append(i+j)
    return l_2mer


def feature_gen(l_2mer, word):  #generate feature for word based on l_2mer
    dict_feature = {}
    for i in l_2mer:
        dict_feature[i] = 0
    for i in range(len(word)-1):
        if word[i]+word[i+1] in l_2mer:
            dict_feature[word[i]+word[i+1]] += 1
    tuple_feature = (sorted(dict_feature.items(), key=lambda e: e[0], reverse=False))  #sort dict_feature according to keys
    data_feature = []
    for i in tuple_feature:
        data_feature.append(i[1])
    return data_feature
