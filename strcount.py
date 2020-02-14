# -*- coding:utf8 -*-
import string
from collections import namedtuple
import numpy as np

def str_count(s):
 
    count_en = count_dg = count_sp = count_zh = count_pu = count_low=0
    

    s_len = len(s)
    for c in s:
        # 英文
        if c in string.ascii_letters:

            count_en += 1
            #小寫
            if c.islower():
                count_low+=1

        # 數字
        elif c.isdigit():
            count_dg += 1
        # 空格
        elif c.isspace():
            count_sp += 1
        # 中文
        elif c.isalpha():
            count_zh += 1
        # 特殊字符
        else:
            count_pu += 1
    result=np.array([[count_zh,count_en,count_dg,count_pu,count_low]], dtype=object)
        


    total_chars = count_zh + count_en + count_sp + count_dg + count_pu
    if total_chars == s_len:
        # return result
        return namedtuple('Count', ['total', 'zh', 'en', 'space', 'digit', 'punc','lower'])(s_len, count_zh, count_en,count_sp, count_dg, count_pu,count_low)
    else:
        print('Something is wrong!')
        return None

if __name__ == '__main__':
    str_l = "這是一個TTTTtest字符串"
    count = str_count(str_l)
    print(str_l, end='\n\n')
    # print('該字符串共有 {} 個字符，其中有 {} 個漢字，{} 個英文，{} 個空格，{} 個數字，{} 個標點符號。{}小寫啦'.format(count.total, count.zh, count.en, count.space,count.digit, count.punc,count.lower))
