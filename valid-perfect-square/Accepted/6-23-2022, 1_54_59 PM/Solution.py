// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        list=[]
        for i in range(1,100000):
            if i*i==num:
                list.append(num)
        if num in list:
            return True

        else:
            return False


        