class Solution:
    def sumOfSeries(self,n):
        #code here
        def cube(n):
            if n>0:
                return (n*n*n)+cube(n-1)
            else:
                return 0

        return cube(n)
        