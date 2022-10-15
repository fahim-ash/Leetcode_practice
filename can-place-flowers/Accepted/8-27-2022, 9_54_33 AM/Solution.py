// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]
        i=1
        l=len(flowerbed)
        while i < l-1:
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1]==0:
                flowerbed[i] =1
                n-=1
            if n<=0:
                return True
            i+=1
        return False
        
        
        
        
        
        