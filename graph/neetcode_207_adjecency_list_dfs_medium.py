"https://leetcode.com/problems/course-schedule/description/"

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        hash_set = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            hash_set[course].append(prereq)

        
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False

            if hash_set[crs] == []:
                return True
            
            visited.add(crs)

            for neighbour in hash_set[crs]:
                if not dfs(neighbour):
                    return False
            visited.remove(crs)
            hash_set[crs] = []
            return True

        for crs in range(numCourses):
            if not  dfs(crs): return False

        return True

