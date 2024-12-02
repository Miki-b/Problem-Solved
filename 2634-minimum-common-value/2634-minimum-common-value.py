import bisect
class Solution:
    def search(self, haystack, needle, start=0):
            find = bisect.bisect_left(haystack, needle, start, len(haystack) - 1)
            if needle == haystack[find]:
                return needle
            else:
                return -1
                
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Edge case for 1 element in array
        if len(nums1) == 1:
            return nums1[0] if nums1[0] in nums2 else -1
        if len(nums2) == 1:
            return nums2[0] if nums2[0] in nums1 else -1

    
        p1, p2 = 0,0
        res = -1
        while p1 < len(nums1) - 1 and p2 < len(nums2) - 1:
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] < nums2[p2]:
                res = self.search(nums1, nums2[p2], p1+1)
                if res != -1:
                    return res
                p2 += 1
            else:
                res = self.search(nums2, nums1[p1], p2+1)
                if res != -1:
                    return res
                p1 += 1
        
        return res