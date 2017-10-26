# -*- coding: UTF-8 -*-
# 题目:
# Given an array of integers, 一列数组
# return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 时间复杂度O(n^2)
        # result = []
        # for j in range(0,len(nums)):
        #     for i in range(j+1,len(nums)):
        #         if nums[j]+nums[i] == target:
        #             result.extend([j,i])
        #             return result
        #         else:
        #             i += 1
        #             if i == len(nums):
        #                 break

        # 时间复杂度O(n)
        for index, ele in enumerate(nums):
            tmp = target - ele
            if tmp in nums[index+1:]:   # 搜索剩下的里面有没有和基本元素配对的,提高效率
                tmp_tuple = nums[index+1:]  # 把剩下的作为一个数组
                return [index, tmp_tuple.index(tmp)+index+1]   # 找到数据的index是新数组的index+第一个元素的index+1(因为新数组的index是从零开始的)


nums = [3,2,4]
target = 6
print twoSum(nums,target)

#Runtime: 32 ms


