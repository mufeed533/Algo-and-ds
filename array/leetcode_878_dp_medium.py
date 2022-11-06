"https://leetcode.com/problems/longest-turbulent-subarray/description/"

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp = [0] * len(arr)
      
        for i in range(len(arr)):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                if arr[i] != arr[i-1]:
                    dp[i] = 2
                else:
                    dp[i] = 1
            else:
                if (arr[i] < arr[i-1] and arr[i-1] > arr[i-2]) or (arr[i] > arr[i-1] and arr[i-1] < arr[i-2]):
                    dp[i] = dp[i-1] + 1
                else:
                    if arr[i] != arr[i-1]:
                        dp[i] = 2
                    else:
                        dp[i] = 1
        return max(dp)


