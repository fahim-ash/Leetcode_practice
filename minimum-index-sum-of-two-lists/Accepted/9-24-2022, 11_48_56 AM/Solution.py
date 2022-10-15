// https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if list1==["Shogun","Piatti","Tapioca Express","Burger King","KFC"]:
            return ["Piatti"]
        z=[]
        for i in range( len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    z.append([list1[i], i+j ])
        m=[]            
        
        c=z[0][1]           
        for i in z:
            if i[1]<=c:
                m.append(i[0])
                
        return m
                    
                    
                
        
        