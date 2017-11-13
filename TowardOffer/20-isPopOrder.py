# -*- coding:utf-8 -*-
# 题目描述

# 输入两个整数序列，
# 第一个序列表示栈的压入顺序，
# 请判断第二个序列是否为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，
# 序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。
# （注意：这两个序列的长度是相等的）

def IsPopOrder(pushV, popV):
    tmp_stack = []
    if pushV is None or popV is None or len(pushV) != len(popV):   # 不符合题意的
        return False
    for i in pushV:
        tmp_stack.append(i)
        while(len(tmp_stack)!=0 and tmp_stack[-1] == popV[0]):
            # len(tmp_stack)!=0是因为只有这样才能比较tmp_stack栈顶元素
            popV = popV[1:]
            tmp_stack.pop()
    if len(tmp_stack):   # 如果len(tmp_stack())!=0 证明所有元素都压入以后还有剩下的没有弹出的元素,所以不是序列
        return False
    return True

pushV = [1,2,3,4,5]
popV1 = [4,5,3,2,1]
popV2 = [4,3,5,1,2]
print IsPopOrder(pushV,popV1)
print IsPopOrder(pushV,popV2)

# 运行时间：28ms
# 占用内存：5632k