# -*- coding:UTF-8 -*-
# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 实际上就是斐波那契数列
# n=1 r=1;n=2 r=2;n=3 r=3;n=4 r=5;n=5 r=8

def jumpFloor(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    list = [1, 2]
    for i in range(2, number):
        list.append(list[i - 2] + list[i - 1])
    return list[-1]

print jumpFloor(3)

# 运行时间 37ms 内存5764k