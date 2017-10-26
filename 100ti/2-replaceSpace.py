# -*- coding:UTF-8 -*-

# 题目描述
# 请实现一个函数，将一个字符串中的空格替换成“%20”。
# 例如，当字符串为We Are Happy.
# 则经过替换之后的字符串为We%20Are%20Happy。

import re

def replaceSpace(s):
    # s = s.replace(' ', '%20')  # 字符串本身的方法
    # return s

    strinfo = re.compile(' ')   # 正则
    s = strinfo.sub('%20', s)
    return s

s = "hello world"
print replaceSpace(s)