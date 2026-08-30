class Solution:
    def bubbleSort(self,arr):
        # code here
        for i in range(len(arr)-1,-1,-1):
            j,count,max=0,0,i
            while j<i:
                if arr[max] < arr[j]:
                    max=j
                j+=1
            arr[i],arr[max]=arr[max],arr[i]
            if count>0:
                break
        return arr