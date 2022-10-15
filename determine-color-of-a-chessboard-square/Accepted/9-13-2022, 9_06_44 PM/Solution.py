// https://leetcode.com/problems/determine-color-of-a-chessboard-square

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        z=["a","c","e","g"]
        c=coordinates
        if c[0] in z:
            if int(c[1]) %2==0:
                return True
            
        else:
            if int(c[1]) %2 !=0:
                return True
            
        return False