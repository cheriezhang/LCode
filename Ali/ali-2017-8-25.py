# -*- coding: UTF-8 -*-
# 阿里巴巴校招笔试附加题2菜鸟仓库货架编号问题
# 题目复述: 仓库编号为0-9整数 以下为一示例：
# 1|   一个货架
# 12|  每个数字是一个格子
# 123|
# 1234|
# 12345|
# ……|12345678910111213141516|…
# 每一个整数代表一个格子，共1千多万个货架，求第k个格子编号
# 输入：货物序号k，一个整数
# 输出：编号
# 输入范例：10
# 输出范例：4

# 理解有误



from math import sqrt
import math


def find(k):
    # 首先确定是哪一个货架  取值范围1-1000万+
    line = sqrt(2 * k)

    if not line.is_integer():
        line = int(line)  # 大致范围
        if (line + 1) * line / 2 < k:  # 需要换到下一行
            line = line + 1
    pos = k - line * (line - 1) / 2

    line_str = ''
    for i in range(1,line+1):
        line_str += str(i)
    print line_str
    print "pos:"+str(pos)




if __name__ == '__main__':  # https://www.zhihu.com/question/49136398 是本模块独有的
    # find(10)
    # find(14)
    # find(21)
    # find(13)
    find(55)
    # find(12)
