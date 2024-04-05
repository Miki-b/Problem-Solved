class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        start=0
        print(1%5)
        while len(arr)>1:
            toberemoved = (start+k-1)%len(arr)
            arr.pop(toberemoved)
            start=toberemoved
        
        
        return arr[0]