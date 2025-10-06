import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # see if in any room we can have this meeting if we can, no extra room needed if not we need an extra room 
        # have a min heap and insert the end meetign time and if the next meetigns start2> end1 then we can use the same room so lets just update this room end time with new end time 
        # if not then add a new room heap [end1,end2,..] so on 
        # but to avoid where we take extra rooms our start tiem intervals should be sorted 
        # test case [5,10] [15,20], [10,15] if we see we can have all these 3 in the same room 
        # and also we should maitain a min heap because lets say after we sorted we have a test case like [5,10],[10,15] [12,16], [15,20] if we wont have min heap then we will take room-1 for [5,10], [10,15] and take room-2 for[12,16] and we take an extra room [15,20] but we can put in the room-1 itself , so we have to maintian a min heap giving us the min time avaliablity rooms 
        
        # tc : O(nlogn) 
        # sc : O(n) min heap space 
        
        # edge case 
        if len(intervals) == 0 :
            return 0
        if len(intervals) ==1:
            return 1
        
        intervals.sort()
        
        meeting_rooms = [intervals[0][0]] # first 
        
        for start, end in intervals: # tc : O(n)
            if meeting_rooms[0] <= start :
                heapq.heappop(meeting_rooms) # pop it and update it with the new end time # O(logn)
                
            # else just add the new room with new end time 
            heapq.heappush(meeting_rooms,end) # O(logn)
            
        return len(meeting_rooms)