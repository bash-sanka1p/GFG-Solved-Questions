from math import gcd, sqrt
class Solution:
    
    def pairCount(self, x, y):
        """code here"""
        n = 0
        res = 0

        if y % x == 0:
            n = y // x

        if n == 1:
            res = 1

        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                j = n // i
                if i != j and gcd(x * i, x * j) == x:
                    res += 2
                    
        return res