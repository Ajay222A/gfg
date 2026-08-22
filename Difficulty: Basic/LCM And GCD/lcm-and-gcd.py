class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        def find_hcf(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        hcf=find_hcf(a,b)
        lcm=(a*b)//hcf
        return [lcm,hcf]