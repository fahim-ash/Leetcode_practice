// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        list=[]
        z=[]
        for i in string.ascii_uppercase:
            z.append(i)
        k=z[z.index(s[0]):z.index(s[3])+1]
        for i in range(int(s[1]),int(s[4])+1):
            for j in k:
                list.append(f"{j}{i}")
        
        list.sort()
            
        return list