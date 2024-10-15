class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max=0
        neg=[]
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
        print(neg)
        for i in range(len(neg)):
            if neg[i]*-1 in nums and neg[i]*-1>max:
                max=neg[i]*-1
        if max==0:
            return -1
        else:
            return max
            



        