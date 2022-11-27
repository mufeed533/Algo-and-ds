"https://leetcode.com/problems/meeting-rooms-ii/description/"

class Solution:
    def minMeetingRooms(self, intervals):
        start_intervals = sorted([i[0] for i in intervals])
        end_intervals = sorted([i[1] for i in intervals])

        room_counter = 0
        max_room_count = 0

        i,j = 0, 0
        while i < len(start_intervals):
            if start_intervals[i] < end_intervals[j]:
                room_counter += 1
                i += 1
            else:
                room_counter -= 1
                j += 1
            max_room_count = max(room_counter, max_room_count)
        
        return max_room_count
    
