// https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    
        list1=[]
        list2=[]
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in list1:
                list1.append(nums1[i])
            elif nums2[i] not in nums1 and nums2[i] not in list2:
                list2.append(nums2[i])
                
        return [list1,list2]
