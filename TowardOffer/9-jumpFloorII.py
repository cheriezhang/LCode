# -*- coding:UTF-8 -*-
# 题目描述
# 一只青蛙一次可以跳上1级台阶，
# 也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 2^(n-1)次方

def jumpFloorII(number):
    return 2**(number-1)

print jumpFloorII(3)

# 运行时间：43ms
# 占用内存：5632k