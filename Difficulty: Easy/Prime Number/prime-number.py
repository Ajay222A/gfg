class Solution:
    def isPrime(self, n):
        # code here
        import math
        if n<=1:
            return False
        limit=int(math.sqrt(n))+1
        for i in range(2,limit):
            if n%i==0:
                return False
        return True
