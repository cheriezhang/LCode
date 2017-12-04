# -*- coding:utf-8 -*-

# 题目描述
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
# 另一个特殊指针指向任意一个节点），
# 返回结果为复制后复杂链表的head。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        self.cloneNodes(pHead)
        self.connectRandomNodes(pHead)
        self.reConnectNodes(pHead)

    def cloneNodes(self,pHead):
        # 将每一个节点都复制一个变成A->A'->B->B'.....
        pNode = pHead
        while pNode is not None:
            pClone = RandomListNode(pNode.label)    # A复制到A' 除了random
            pClone.next = pNode.next     # 把A'指向B
            pNode.next = pClone          # 把A和A'链接起来
            pNode = pClone.next          # 重新指定pHead->B

    def connectRandomNodes(self,pHead):
        pNode = pHead
        while pNode is not None :   # A,B,C....
            pClone = pNode.next     # A',B',C'....
            if pNode.random is not None:   # 如果A有random,将其复制到A'
                pClone.random = pNode.random.next
            pNode = pClone.next

    def reConnectNodes(self,pHead):
        pNode = pHead
        pCloneHead = None
        pCloneNode = None

        if pNode != None:   # 如果有原头结点 A
            pCloneHead = pCloneNode = pNode.next  # 设置新的克隆头结点和中间节点,初始化新的链表 A'
            pNode.next = pCloneNode.next    # 将A指向B         A->next = A'->next
            pNode = pNode.next              # 新的pNode为B     pNode = A->next = B

        while pNode != None:   # 从B开始循环
            pCloneNode.next = pNode.next    # 将A'指向B'
            pCloneNode = pCloneNode.next    # 新的pCloneNode为B'
            pNode.next = pCloneNode.next    # B->next = B'->next = C
            pNode = pNode.next              # pNode = C

        return pCloneHead


# 运行时间：28ms
# 占用内存：5760k




