# -*- coding:UTF-8 -*-
# 题目描述
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

def minNumberInRotateArray(rotateArray):
    size = len(rotateArray)
    if size == 0:
        return 0
    else:
        while size >= 1:
            if size == 1:
                return rotateArray[0]
            else:
                if size%2==0:
                    index = size/2-1
                else:
                    index = size/2
                tmp = rotateArray[index]  # 中间值
                if tmp-rotateArray[-1] >= 0:   # 该数字不是旋转的那部分
                    rotateArray = rotateArray[index+1:]
                else:   # 该数字是旋转的部分
                    rotateArray = rotateArray[:index+1]
                size = len(rotateArray)


rotateArray = [3,4,5,1,2,3]
print minNumberInRotateArray(rotateArray)

# 运行时间 1229ms 内存5632k