class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new= set(nums2)
        ans=[]
        for i in nums1:
            if i in new:
                ans.append(i)
                new.remove(i)
        return ans
            



        