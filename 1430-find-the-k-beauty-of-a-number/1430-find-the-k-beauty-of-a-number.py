class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        L=0
        count=0
        new=str(num)
        for i in range(len(new)):
            if i-L+1==k:
                if int(new[L:i+1])!=0 and num%int(new[L:i+1])==0:
                    count+=1
               
                L+=1
        return count
