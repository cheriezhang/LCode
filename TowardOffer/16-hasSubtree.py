# -*- coding:utf-8 -*-
# 题目描述
# 输入两棵二叉树A，B，判断B是不是A的子结构。
# （ps：我们约定空树不是任意一个树的子结构）

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 遍历A 找到与B的根节点相同的节点,然后同时遍历A,B
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                result = self.isSubtree(pRoot1, pRoot2)
            if (not result):
                result = self.isSubtree(pRoot1.left, pRoot2)
            if (not result):
                result = self.isSubtree(pRoot1.right, pRoot2)
        return result

    def isSubtree(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSubtree(pRoot1.left, pRoot2.left) and self.isSubtree(pRoot1.right, pRoot2.right)

# 运行时间：31ms
# 占用内存：5760k