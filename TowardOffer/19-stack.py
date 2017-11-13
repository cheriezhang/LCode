# -*- coding:utf-8 -*-
# 题目描述
# 定义栈的数据结构
# 请在该类型中实现一个能够得到栈最小元素的min函数。

class Solution:
    def __init__(self):
        self.m_data = []  # 数据栈
        self.m_min = []    # 最小值栈
    def push(self, node):
        # 比较
        self.m_data.append(node) # 加入数据栈
        # 加入最小值栈
        if self.m_min == [] or node < self.m_min[-1]: # 如果最小值栈等于空或者推进来的元素<node
            self.m_min.append(node)  # 加入数据栈
        else:
            self.m_min.append(self.m_min[-1])
        # 两个栈都push

    def pop(self):   # 弹出栈顶元素
        if self.m_data == []:
            return
        else:
            self.m_data.pop()
            self.m_min.pop()

    def top(self):  # 获取栈顶元素
        return self.m_data[-1]
    def min(self):
        return self.m_min[-1]

    # 运行时间：30ms
    # 占用内存：5640k