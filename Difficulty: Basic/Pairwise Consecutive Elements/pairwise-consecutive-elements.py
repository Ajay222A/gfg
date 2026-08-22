class Solution:
    def pairWiseConsecutive(self, st: list[int]) -> bool:
        # code here
        l,r=0,1
        if len(stack)%2==1:
            while r<len(st)-1:
                if st[l]-st[r]==1 or st[l]-st[r]==-1:
                    l+=2
                    r+=2
                else:
                    return False
            else:
                return True
        else:    
            while r<len(st):
                if st[l]-st[r]==1 or st[l]-st[r]==-1:
                    l+=2
                    r+=2
                else:
                    return False
            else:
                return True