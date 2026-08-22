class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        le=len(arr)
        mid=(le+1)//2 
        if le%2!=0:
            return arr[mid-1]
        else:
            r=(arr[mid-1]+arr[mid])/2
            return r 
