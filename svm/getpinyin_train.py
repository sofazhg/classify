#! /usr/bin/python3
# encoding: utf-8

"""
@author: Shaohua Zhang
@contact: sofazhg@outlook.com
@file: getpinyin_train.py
@time: 2019-03-14 22:20
"""

import os
import sys
import string
import xpinyin
import time
import random
from xpinyin import Pinyin

start = time.process_time()


def GBK2312():  #Common Chinese characters encoded by GBK2312
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb18030')
    return str


p = Pinyin()
num_str = 35536  #the same number of different words in eng.txt
filter1 = str.maketrans('', '', '犭扌艹衤忄氵')  #filter characters that cannot be decoded by xpinyin
pinyin_train = open(r'./temp/pinyin_train.txt', mode='w', encoding='utf-8')
for i in range(num_str):
    characters = ''
    len_character = random.randint(1, 5)  #get 1 to 5 Chinese characters
    for i in range(len_character):
        characters = characters + str(GBK2312())
    temp = p.get_pinyin(characters, '')  #transfer Chinese characters into their pinyin
    temp = temp.translate(filter1)
    pinyin_train.write(temp + '\n')  #get pinyin of number num_str

pinyin_train.close()

end = time.process_time()
print('Program processing time：')
print(str(end - start))
