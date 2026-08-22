class Solution:
    def deleteMid(self, s):
        # code here
        mid=(len(s)+1)//2
        s.pop(mid-1)