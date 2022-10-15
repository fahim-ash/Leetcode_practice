// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        list1=0
        list2=0
        for i in seats:
            if i not in students:
                list1+=i
        for j in students:
            if j not in seats:
                list2+=j
                

        return abs(list1-list2)
            
        