class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if low<high:
            partition_index=self.partition(arr,low,high)
            self.quickSort(arr,low,partition_index-1)
            self.quickSort(arr,partition_index+1,high)
        return arr

    def partition(self, arr, low, high):
        # code here
        if low<high:
            pivot_index=arr[low]
            i=low+1
            j=high
            while i<=j:
                while (i<=j and arr[i]<=pivot_index):
                    i+=1
                while (j>=i and pivot_index<arr[j]):
                    j-=1
                if i<j:
                    arr[i],arr[j]=arr[j],arr[i]
            arr[low],arr[j]=arr[j],arr[low]
            return j
