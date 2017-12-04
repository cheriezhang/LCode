# -*- coding:utf-8 -*-

# 题目描述
# 输入一棵二叉搜索树，(左节点比根小,右节点比根大)
# 将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#   10
#  6   14
# 4 8 12 16
class Solution:
    def Convert(self, pRootOfTree):
        # 只有一个点的树或者没有节点的树
        if not pRootOfTree:
            return pRootOfTree

        # 如果是叶节点,就返回叶节点本身
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # 中序遍历——左根右
        # 如果不是空树或者叶节点,处理左子树
        self.Convert(pRootOfTree.left)   # 进入倒数第二层的左子树
        left = pRootOfTree.left   # 左叶节点

        # 连接左子树
        if left:     # 如果有左叶节点
            while(left.right):  # 看左节点有没有右节点
                left = left.right
            pRootOfTree.left = left   # 6的左边是4
            left.right = pRootOfTree  # 4的右边是6

        # 处理右子树
        self.Convert(pRootOfTree.right)  # 6的右节点
        right = pRootOfTree.right    # right = 8

        # 连接根与右子树最小结点
        if right:
            while (right.left):
                right = right.left
            pRootOfTree.right = right  # 6的右边是8
            right.left = pRootOfTree   # 8的左边是6

        while (pRootOfTree.left):      # 如果6有节点
            pRootOfTree = pRootOfTree.left  # 新的根节点是4
        return pRootOfTree  # 返回4

# 运行时间：33ms
# 占用内存：5632k
