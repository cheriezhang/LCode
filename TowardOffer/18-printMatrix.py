# -*- coding:utf-8 -*-
# 题目描述
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字.
# 例如，如果输入如下矩阵：
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
# 则依次打印出数字
# 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10

def printMatrix(matrix):
    if not matrix:
        return None
    rows = len(matrix)  # 有几行
    columns = len(matrix[0])  # 有几列
    res = []
    start = 0
    while (columns > 2 * start and rows > 2 * start):
        # 打印一圈
        res.extend(printCircle(matrix, start, rows, columns))
        start += 1
    return res


def printCircle(matrix, start, rows, cols):
    endX = cols - start -1
    endY = rows - start -1
    result = []
    # 打印上面一行
    for i in range(start, endX+1):
         result.append(matrix[start][i])
         # print matrix[start][i]
    # 打印右边一列
    if start < endY:
        for j in range(start + 1, endY+1):
            result.append(matrix[j][endX])
            # print matrix[j][endY - 1]
    # 打印下面一行
    if start < endX and start< endY:
        for k in range(endX - 1, start - 1, -1):
            result.append(matrix[endY][k])
    # 打印左边
    if start < endX and start < endY-1:
        for p in range(endY - 1, start, -1):
            result.append(matrix[p][start])
    return result


A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

B = [[1], [2], [3], [4]]

C = [1,2,3,4,5]
print printMatrix(A)
print printMatrix(B)
#print printMatrix(C)

# 运行时间：34ms
# 占用内存：5504k