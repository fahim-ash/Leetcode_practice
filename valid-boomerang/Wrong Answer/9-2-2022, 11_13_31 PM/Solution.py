// https://leetcode.com/problems/valid-boomerang

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        count=abs(points[0][0]-points[0][1])
        
        
        z=[]
        
        for i in points:
            if i in z:
                return False
            else:
                z.append(i)
                
        list=[]
        
        for i in points:
            list.append(abs(i[0]-i[1]))
               
        x=[]
        for i in list:
            if i in x:
                return False
            else:
                x.append(i)
        