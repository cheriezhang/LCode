# -*- coding:utf-8 -*-
# 题目描述

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。
# 假设输入的数组的任意两个数字都互不相同。

# 后序遍历: 左右根?
# 二叉搜索树: 空树或者
# 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
# 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
# 测试用例: 5,7,6,9,10,11,8
# 最后一个是根节点 比根节点大的是右子树,比根节点小的是左子树

def VerifySquenceOfBST(sequence):
    if len(sequence) == 0:
        return False
    if len(sequence) == 1:
        return True
    i = 0
    while sequence[i] < sequence[-1]:  # 看在哪里分界的,找到第一个大于根节点的值
        i = i + 1
    k = i  # 保存分界值
    for j in range(i, len(sequence) - 1):    # 不包括根节点的节点和根节点比较
        if sequence[j] < sequence[-1]:  # 右子树中有小于根节点的值
            return False
    left_tree = sequence[:k]  # 能够保证都小于根节点
    right_tree = sequence[k:len(sequence) - 1]  # 没有return False 能够保证都大于根节点

    left = True
    right = True
    if len(left_tree) > 0:
        left = VerifySquenceOfBST(left_tree)
    if len(right_tree) > 0:
        right = VerifySquenceOfBST(right_tree)
    return left and right


sequence = [4, 6, 7, 5]
print VerifySquenceOfBST(sequence)

# 运行时间：45ms
# 占用内存：5888k
