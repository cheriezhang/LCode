# -*- coding:UTF-8 -*-

# 题目描述
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
# F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*)
# n<=39
def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    list = [0,1]
    for i in range(2,n+1):
        list.append(list[i-2]+list[i-1])
    return list[-1]


print Fibonacci(0)

# 运行时间 32ms
# 内存5764k