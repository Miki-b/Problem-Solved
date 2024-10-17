class Solution:
    def maxArea(self, height: List[int]) -> int:
        max=0
        i,j=0,len(height)-1
        while i<j:
            if height[i]>height[j]:
                x=height[j]
                y=j-i
                j-=1
            else:
                x=height[i]
                y=j-i
                i+=1
            if x*y>max:
                max=x*y
        return max
            
                


        