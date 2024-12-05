class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ans,i,j=0,0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            
        return -1


        
        