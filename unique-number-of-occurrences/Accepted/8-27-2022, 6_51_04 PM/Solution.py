// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        obj={}
        list=[]
        for i in arr:
            obj[i]=i
            
        for i in obj:
            count=0
            for j in arr:
                if i==j:
                    count+=1
            if count not in list:
                list.append(count)
            else:
                return False
        return True
        
        
        