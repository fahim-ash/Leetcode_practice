// https://leetcode.com/problems/sum-of-all-odd-length-subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(0,len(arr) + 1,2):
            for j in range(len(arr) - i):
                ans += sum(arr[j:j+ i + 1])
                
                
        return ans
        
        