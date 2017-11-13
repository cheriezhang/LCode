# -*- coding:UTF-8 -*-
# 题目描述

# 输入一个链表，输出该链表中倒数第k个结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        k_node = head  # 最后存储结果的指针
        n_node = head  # 遍历到最后的指针
        if k == 0 or head is None:
            return

        for i in range(k - 1):
            if n_node.next is not None:
                n_node = n_node.next  # 移到k-1节点
            else:
                return

        while (n_node.next is not None):
            n_node = n_node.next
            k_node = k_node.next

        return k_node


listNode = ListNode(1)
listNode.next = ListNode(2)
result = Solution()
print result.FindKthToTail(listNode, 3)

# 运行时间：32ms
# 占用内存：5756k
