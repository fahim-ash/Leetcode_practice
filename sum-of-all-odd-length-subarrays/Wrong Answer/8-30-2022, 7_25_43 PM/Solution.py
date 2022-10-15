// https://leetcode.com/problems/sum-of-all-odd-length-subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        count=0
        for i in arr:
            count+=i
            
        countSec=0
        
        if len(arr) >=3:
            for i in range (len(arr)-2):
                print(arr[i],arr[i+1],arr[i+2])
                countSec+=arr[i]+arr[i+1]+arr[i+2]
        
        countThree=0
        if len(arr)%2==1 and len(arr)>3:
            countThree=count+countThree
        print(count,countSec,countThree)
        return (countSec+count+countThree)
        