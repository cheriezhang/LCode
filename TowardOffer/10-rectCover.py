# -*- coding:UTF-8 -*-
# 题目描述
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形
# 总共有多少种方法？
# 斐波那契数列
# # n=1 r=1;n=2 r=2;n=3 r=3;n=4 r=5;n=5 r=8

def rectCover(number):
    if number==0:
        return 0
    if number==1:
        return 1
    if number==2:
        return 2
    list = [1,2]
    for i in range(2,number):
        list.append(list[i-2]+list[i-1])
    return list[-1]

print rectCover(4)

# 运行时间：37ms
# 占用内存：5760k