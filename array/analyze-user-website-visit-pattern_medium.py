"https://leetcode.com/problems/analyze-user-website-visit-pattern/description/"

from itertools import combinations

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """

        input_data = []
        for index in range(len(username)):
            input_data.append((timestamp[index], str(username[index]), str(website[index])))
        input_data = sorted(input_data)
        
        user_visit = {}
        for entry in input_data:
            user_name = entry[1]
            website = entry[2]

            if user_name not in user_visit:
                user_visit[user_name] = []
            
            user_visit[user_name].append(website)
        
        combinations_map = {}
        for user, visit in user_visit.items():
            all_combinations = set(combinations(visit, 3))
            for comb in all_combinations:
                combinations_map[comb] = 1 + combinations_map.get(comb, 0)
        def sortedKey(pattern):
            return  -combinations_map[pattern],pattern


        return sorted(combinations_map, key = sortedKey)[0]

