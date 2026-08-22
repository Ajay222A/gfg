class Solution:
    
    #  Push elements of an array into a stack.
    def push(self, arr):
        # code here
        self.stack=[]
        for a in arr:
            self.stack.append(a)
    #  Print elements of a stack and pop them.
    def printAndPop(self, stack):
        for i in range(len(self.stack)):
            d=self.stack.pop()
            print(d,"",end="")
        # code here
