# -*- coding:utf-8 -*-
# 题目描述
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        result = []
        if root is None:
            return result
        tmp = [root]  # 存储当前层的节点
        while(len(tmp)):
            t = tmp.pop(0)   # tmp中既pop了,又把pop中的值给了t
            result.append(t.val)
            if t.left is not None:
                tmp.append(t.left)
            if t.right is not None:
                tmp.append(t.right)
        return result

# 运行时间：31ms
# 占用内存：5648k
