// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary

class Solution:
    def average(self, salary: List[int]) -> float:
        max= 0
        min= salary[0]
        count=0
        for i in salary:
            count+=i
            if i>max:
                max=i
                
            elif i<min:
                min=i
            
        
        return (count-(min+max)) / (len(salary)-2)