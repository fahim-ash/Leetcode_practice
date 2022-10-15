// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        res=0
        l=[]
        s=sum(nums)
        for i in t:
            res+=i
            s=s-i
            if res<=s:
                l.append(i)
            else:
                l.append(i)
                return l