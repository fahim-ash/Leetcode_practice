// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        arr = [nums[i+1] for i in range(len(nums)-1) if nums[i] == key]
        d = Counter(arr)
        return max(d, key = d.get)
        

        