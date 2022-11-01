Link : https://leetcode.com/problems/group-anagrams/submissions/834531597/

Solution:
class Solution(object):
    def get_ord(self, s):
        return 26 - (ord("z") - ord(s))

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        for i in strs:
            temp = [0] * 26
            for j in i:
                temp[self.get_ord(j) - 1] += 1
            
            if tuple(temp) not in anagrams:
                anagrams[tuple(temp)] = []
            anagrams[tuple(temp)].append(i)
        
        result = []
        for value in anagrams.values():
            result.append(value)
        return result

