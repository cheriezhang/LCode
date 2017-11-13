# -*- coding:utf-8 -*-
# 题目描述:
# 操作给定的二叉树，将其变换为源二叉树的镜像。
# 输入描述:
# 二叉树的镜像定义：源二叉树
#     	    8
#     	   /  \
#     	  6   10
#     	 / \  / \
#     	5  7 9   11
#     	镜像二叉树
#     	    8
#     	   /  \
#     	  10   6
#     	 / \  / \
#     	11 9  7  5


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 迭代遍历 交换左右节点
class Solution:
    def Mirror(self,root):
        # write code here
        if root is None:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        if root.left is not None:
            self.Mirror(root.left)
        if root.right is not None:
            self.Mirror(root.right)
            
# 运行时间：38ms
# 占用内存：5632k