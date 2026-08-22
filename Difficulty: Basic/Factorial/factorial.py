class Solution:
    def factorial(self, n: int) -> int:
        # code here
        
        r=1
        for i in range(1,n+1):
            r=r*i
        return r