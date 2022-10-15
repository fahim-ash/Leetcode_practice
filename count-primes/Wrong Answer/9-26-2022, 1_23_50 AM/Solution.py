// https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        count=0
        list=[]
        if n<2:
            return 0
        for nums in range(2,n):
            
            for i in range(2,nums):
                if nums%i==0:
                    
                    break
                
                else:
                    if nums not in list:
                        list.append(nums)
                        
        return len(list)