"https://leetcode.com/problems/search-a-2d-matrix/submissions/837227012/"
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if i:
                if i[0] <= target and i[-1] >= target:
                    s, e= 0, len(i) - 1
                    
                    while s <= e:
                        mid = (s+e) // 2
                        if i[mid] == target:
                            return True
                        elif i[mid] < target:
                            s = mid + 1
                        else:
                            e = mid - 1
        
        return False

