class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        low=0
        high=len(nums)-1
        def rev(nums,low,mid,high):
            temp=[]
            right=mid+1
            left=low
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else: 
                    temp.append(nums[right])
                    right+=1
            while left<=mid:
                temp.append(nums[left])
                left+=1
            while right<=high:
                temp.append(nums[right])
                right+=1
            
            for i in range(len(temp)):
                nums[i+low]=temp[i]
            
        def mergeSort(nums,low,high):
            if low>=high:
                return 
            mid=(high+low)//2
            mergeSort(nums,low,mid)
            mergeSort(nums,mid+1,high)
            rev(nums,low,mid,high)
        mergeSort(nums,low,high)
        return nums
        
        
                
            
        