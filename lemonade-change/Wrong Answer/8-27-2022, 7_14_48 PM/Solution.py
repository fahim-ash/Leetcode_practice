// https://leetcode.com/problems/lemonade-change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        twenty=0
        
        for i in bills:
            if i==5:
                five+=5
            elif i==10:
                ten+=10
            elif i==20:
                twenty+=20
        z=five+ten+twenty
        for i in bills:
            if i==10:
                if five>=10:
                    five=five-10
                elif five==0:
                    return False
                    
            if i==20:
                if z>=20:
                    z=z-20
                elif z==0:
                    return False
                
        return True
                    
                
            
        