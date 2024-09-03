class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new=[0 for _ in range(len(nums)-1)]
        duplicate=0
        for i in range(len(nums)):
            if nums[i]!=new[nums[i]-1]:
                new[nums[i]-1]=nums[i]
            else:
                duplicate=nums[i]
                break
        return duplicate

        