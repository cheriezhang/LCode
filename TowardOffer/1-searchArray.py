# -*- coding:UTF-8 -*-

# 题目描述:
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

def searchArray(target,array):
    ####### my idea ########
    result = False
    h = len(array)   # 数组高
    w = len(array[0])   # 数组宽
    time = min(h, w)
    for i in range(time):
        if target >= array[i][i]:   # 找对角线
            if target in array[i]:  # 行搜索
                result = True
            else:
                for j in range(i,h):
                    if target == array[j][i]:
                        result = True
    return result

    ######## book's idea ########
    # 从右上角开始搜索

Array = [[1,2,8,9],[4,7,10,13]]
target = 7

searchArray(target,Array)


