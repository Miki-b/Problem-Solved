class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        mini=float('inf')
        Left=0
        Right=len(nums)-1
        nums.sort()
        for i in range(len(nums)//2):  
            mini=min(mini,(float(nums[Left]+nums[Right])/float(2)))
            Left+=1
            Right-=1
        return mini


        