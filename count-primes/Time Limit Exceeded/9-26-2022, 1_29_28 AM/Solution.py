// https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        answer = 0 
        if n == 0 or n == 1:
            return 0 
        
		
        for prime in range(2, n):
            for divisor in range(2, prime):
                if prime % divisor == 0:
                    break 
            else:
                answer += 1
        return answer