// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        nums2=[]

        for i in range(nums.index(key)+1,len(nums)):
            nums2.append(nums[i])


        most= max(nums2,key=nums2.count)
        return most



        