// https://leetcode.com/problems/merge-similar-items

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort()
        items2.sort()
        
        z=None
        
        if len(items1)<len(items2):
            z=items1
        else :
            z=items2
            
        for i in range(len(z)):
            for j in range(len(z)):
                if items1[j]==items2[j]:
                    if z==items1:
                        items2[i][-1]= items1[i][-1]+items2[i][-1]
                    elif z==items2:
                        items1[i][-1]= items1[i][-1]+items2[i][-1]
                
            
        if z==items1:
            return items2
        else :
            return items1
    
        