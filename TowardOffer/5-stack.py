# -*- coding:UTF-8 -*-

# 题目描述
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。
# 队列中的元素为int类型。
# 队尾插入节点,队头pop节点


class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2 == []:
            while len(self.stack1) != 0:  #还有元素的话
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

