"https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/submissions/837543155/"

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        l = 0
        total = 0
        result = 0

        for r in range(len(arr)):
            if (r - l + 1) > k:
                total -= arr[l]
                l += 1
            
            total += arr[r]
            if (r - l + 1) == k and (total / k) >= threshold:
                result += 1
            
        return result
