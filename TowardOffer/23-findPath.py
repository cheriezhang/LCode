# -*- coding:utf-8 -*-
# 题目描述

# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

def FindPath(root, expectNumber):
    if not root:   # 如果是一棵空树,则返回路径为空
        return []
    if root.left is None and root.right is None and root.val == expectNumber:
        # 如果当前节点没有左右节点(为叶节点),且当前节点的值等于需要的值(是减去前面节点值之后的)
        return [[root.val]]
    res = []
    left = FindPath(root.left, expectNumber - root.val)
    right = FindPath(root.right, expectNumber - root.val)
    for i in left + right:
        res.append([root.val] + i)
    return res

