"https://leetcode.com/problems/meeting-rooms/description/"

class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key = lambda x : x[0])
        
        for index in range(len(intervals[:-1])):
            if intervals[index+1][0] < intervals[index][1]:
                return False
        
        return True

