# -*- coding:UTF-8 -*-
# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。


# def get_binary_list(self,x):
#     b_list = []
#     tmp_list = []
#     if x==0:
#         b_list.append(0)
#     else:
#         while (x!= 0):
#             exp = 0
#             while (x >= 2 ** exp):
#                 exp += 1
#             tmp_list.append(exp-1)
#             x = x - 2 ** (exp-1)
#
#         for i in range(tmp_list[0]+1):
#             if i in tmp_list:
#                 b_list.append(1)
#             else:
#                 b_list.append(0)
#     return b_list
#
#
# def NumberOf1(self,n):
#     # 首先判断正数(包括0)还是负数
#     if n >= 0:
#         bin = self.get_binary_list(n)
#         return sum(bin)
#     else:
#         n = abs(n)
#         yuanma = self.get_binary_list(n)
#         fanma = [1-i for i in yuanma]
#         for i in range(len(fanma)):
#             if fanma[i] == 1:
#                 fanma[i]=0
#             else:
#                 fanma[i]=1
#                 break
#         return sum(fanma)


# 因为负数在内存中是以补码形式存在的，
# 所有首先根据负数的原码求出负数的补码(符号位不变，其余位按照原码取反加1)，
# 然后保证符号位不变，其余位向右移动到X位，在移动的过程中，高位补1.
# 等移位完成以后，然后保持符号位不变，其余按位取反加1，得到移位后所对应数的原码。即为所求。

# -5
# 原码(8位) 00000101
# 反码      11111010
# 补码      11111011   (计算机中存储的形式)
# 因此求有几个1 就是和00000001与并不断右移
# 11111011  与
# 00000001
# =00000001 说明最后一位是1

def NumberOf1(n):
    list_1= []
    for i in range(0,32):
        list_1.append(n>>i & 1)
    return sum(list_1)
    # return sum([(n>>i & 1) for i in range(0,32)]) # 简单形式
print NumberOf1(288)

# 运行时间：41ms
# 占用内存：5632k