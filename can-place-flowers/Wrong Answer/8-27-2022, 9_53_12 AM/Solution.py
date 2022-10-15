// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        z=(len(flowerbed)-2)//2
        if z==n and z%2==0:
            return False
        if (len(flowerbed)-2)//2 >=n:
            return True
        
        
        
        
        