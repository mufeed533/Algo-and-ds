"https://leetcode.com/problems/product-of-array-except-self/description/"

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre_mul = [1 for i in range(len(nums))]
        post_mul = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                pre_mul_prod = 1
                pre_mul[i] = 1 
                continue
            pre_mul_prod = nums[i -1] * pre_mul_prod
            pre_mul[i] = pre_mul_prod
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                post_mul_prod = 1
                post_mul[i] = 1 
                continue
            post_mul_prod = nums[i + 1] * post_mul_prod
            post_mul[i] = post_mul_prod
        
        return [pre_mul[i] * post_mul[i] for i in range(len(pre_mul))]
        

