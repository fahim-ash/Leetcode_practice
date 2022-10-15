// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        nums2=[]
        nums3=[]
        for i in range(nums.index(key)+1,len(nums)):
            nums2.append(nums[i])
        for i in range(nums2.index(key)+1,len(nums2)):
            nums3.append(nums2[i])

        most= max(nums3,key=nums3.count)
        return most



        