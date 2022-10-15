// https://leetcode.com/problems/two-out-of-three

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        z=[]
        for i in nums1:
                for k in nums2:
                        for j in nums3:
                                if i==k or i==j :
                                        z.append(i)
                                        z.append(k)
                                        z.append(k)
        z = list(dict.fromkeys(z))
        return z
        