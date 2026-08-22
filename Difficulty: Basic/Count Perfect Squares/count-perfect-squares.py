class Solution:
    def countSquares(self, n):
        # code here 
        def sq(n):
            for i in range(1,n):
                t=i
                if i*i >= n:
                    return t-1
        result=sq(n)
        return result
                