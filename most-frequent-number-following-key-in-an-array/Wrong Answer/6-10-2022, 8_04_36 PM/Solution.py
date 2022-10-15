// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        nums.remove(key)
        most= max(nums,key=nums.count)
        return most
        