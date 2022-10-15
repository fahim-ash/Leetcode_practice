// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        for i in range(len(nums)):
            if nums[i]==key:
                nums.remove(key)
                break

        most= max(nums,key=nums.count)
        return most


        