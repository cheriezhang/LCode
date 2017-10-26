# -*- coding:UTF-8 -*-

# 题目描述
# 输入一个链表，从尾到头打印链表每个节点的值。
# 返回从尾部到头部的列表值序列，例如[1,2,3]

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

listNodeR = {}
def printListFromTailToHead(listNode): # 实际上是倒序输出
    list = []
    head = listNode
    while head:
        list.insert(0, head.val)
        head = head.next
    return list

print printListFromTailToHead(listNodeR)

