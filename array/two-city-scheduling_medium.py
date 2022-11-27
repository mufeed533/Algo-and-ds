"https://leetcode.com/problems/two-city-scheduling/description/"

class Solution:
    def twoCitySchedCost(self, costs):
        difference_list = []
        for idx in range(len(costs)):
            a_cost, b_cost = costs[idx]
            difference_list.append([b_cost - a_cost, idx])
        difference_list.sort(key = lambda x: x[0])
        mid_val = len(difference_list) // 2
        b_city_values = [costs[i[1]][1] for i in difference_list[:mid_val]]
        a_city_values = [costs[i[1]][0] for i in difference_list[mid_val:]]
        return sum(b_city_values) + sum(a_city_values)
        
