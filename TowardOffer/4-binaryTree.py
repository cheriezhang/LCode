# -*- coding:UTF-8 -*-

# 题目描述
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建二叉树并返回。
# 前序遍历,根左右
# 中序遍历,左根右

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 返回构造的TreeNode根节点


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0]).val
        else:
            flag = TreeNode(pre[0])
            flag.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])])
            flag.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:] )
        return flag


# def reConstructBinaryTree(pre, tin):
#     # write code here
#     result = []
#     # 初始化
#     root = pre[0]
#     result.append(root)
#
#     leftTreetin = tin[:tin.index(root)]
#     rightTreetin = tin[tin.index(root) + 1:]
#
#     if len(leftTreetin) != 0:
#         leftTreepre = pre[1:1+len(leftTreetin)]
#     if len(rightTreetin) != 0:
#         rightTreepre  = pre[-len(rightTreetin):]
#
#
#     while len(leftTreepre)!=0 or len(rightTreepre) !=0:   # 左或右有子树
#
#         if len(leftTreepre)!=0:   # 有左子树
#             print "leftTreepre"
#             root = leftTreepre[0]  # 找出根节点 leftTreepre相当于之前的pre
#             result.append(root)
#             tin = leftTreetin
#             print tin
#             pre = leftTreepre
#             print pre
#             leftTreetin = tin[:tin.index(root)]
#             rightTreetin = tin[tin.index(root) + 1:]
#             if len(leftTreetin) != 0:
#                 leftTreepre = pre[1:1 + len(leftTreetin)]
#             if len(rightTreetin) != 0:
#                 rightTreepre = pre[-len(rightTreetin):]
#
#             # leftTreetin = leftTreetin[:leftTreetin.index(root)]   # leftTreetin相当于原来的tin
#             # rightTreetin = leftTreetin[leftTreetin.index(root) + 1:]  # 相对的右子树
#             # if len(leftTreetin) != 0:
#             #     leftTreepre = leftTreepre[1:1 + len(leftTreetin)]
#             # if len(rightTreetin) != 0:
#             #     rightTreepre = leftTreepre[-len(rightTreetin):]
#
#
#         if len(rightTreepre)!=0:  # 有右子树
#             print "rightTreepre"
#             root = rightTreepre[0]
#             result.append(root)
#             tin = rightTreetin
#             print tin
#             pre = rightTreepre
#             print pre
#             leftTreetin = tin[:tin.index(root)]
#             rightTreetin = tin[tin.index(root) + 1:]
#             if len(leftTreetin) != 0:
#                 leftTreepre = pre[1:1 + len(leftTreetin)]
#             if len(rightTreetin) != 0:
#                 rightTreepre = pre[-len(rightTreetin):]
#             # leftTreetin = rightTreetin[:rightTreetin.index(root)]
#             # rightTreetin = rightTreetin[rightTreetin.index(root) + 1:]
#             # if len(leftTreetin) != 0:
#             #     leftTreepre = rightTreepre[1:1 + len(leftTreetin)]
#             # if len(rightTreetin) != 0:
#             #     rightTreepre = rightTreepre[-len(rightTreetin):]
#         return result
    def printTree(self,pre,tin):
        print self.reConstructBinaryTree(pre, tin)

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
R = Solution()
R.printTree(pre,tin)