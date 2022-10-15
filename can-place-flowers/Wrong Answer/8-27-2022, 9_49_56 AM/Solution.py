// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        print((len(flowerbed)-2)//2)
        return (len(flowerbed)-2)//2 >=n
        
        
        