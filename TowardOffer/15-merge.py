# -*- coding:UTF-8 -*-
# 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表
# 当然我们需要合成后的链表满足单调不减规则。

# 递归方法:
class Solution:
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        if pHead2.val >= pHead1.val:
            pHead1.next = self.Merge(pHead1.next,pHead2)
            return pHead1   # 在第一次执行merge之后头结点是pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2

# 运行时间：28ms
# 占用内存：5752k

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 非递归 失败~
# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         if pHead1 is None:
#             return pHead2
#         if pHead2 is None:
#             return pHead1
#
#         result = None  # 头节点
#         tmp = None # 工作节点
#
#         while pHead1 is not None and pHead2 is not None:
#             if pHead2.val>= pHead1.val:
#                 if result is None:
#                     result = tmp = pHead1
#                 else:
#                     tmp.next = pHead1
#                     tmp = tmp.next
#                 pHead1.next = pHead1
#             else:
#                 if result is None:
#                     result = tmp = pHead2
#                 else:
#                     tmp.next = pHead2
#                     tmp = tmp.next
#                 pHead2.next = pHead2
#
#         if pHead1 is None:
#             tmp.next = pHead2
#         else:
#             tmp.next = pHead1
#         return result
