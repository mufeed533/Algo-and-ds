Link : https://leetcode.com/problems/top-k-frequent-elements/submissions/834539847/

Solution:
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        max_frequency = 0

        for i in nums:
            frequency[i] = 1 + frequency.get(i, 0)
            max_frequency = max(max_frequency, frequency[i])
        
        frequency_arr =  [[] for j in range(max_frequency)]
        
        for n, f in frequency.items():
            frequency_arr[f - 1].append(n)
        
        result = []
        for i in frequency_arr[::-1]:
            for j in i:
                result.append(j)
                if len(result) == k:
                    return result
        return result

        
