# -*- coding:UTF-8 -*-
# 题目描述
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。

def reOrderArray(array):
    array_ji = []
    array_ou = []
    for item in array:
        print item
        if item % 2 == 0:  # ou
            array_ou.append(item)
        else:
            array_ji.append(item)
    # return array_ji+array_ou  # 新数组
    array_ji.extend(array_ou)
    return array_ji  # 旧数组


aray = [1, 2, 3, 4, 5, 6, 7]
print reOrderArray(aray)

# 运行时间：40ms
# 占用内存：5764k
