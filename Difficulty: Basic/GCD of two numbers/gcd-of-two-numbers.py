class Solution:
    def gcd(self, a, b):
        # code here
        def g_hcf(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        hcf=g_hcf(a,b)
        return hcf