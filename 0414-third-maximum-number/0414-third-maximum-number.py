class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        L=len(nums)
        ans=[]
        nums = list(dict.fromkeys(nums))
        nums.sort()
        print(nums)
        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]

             