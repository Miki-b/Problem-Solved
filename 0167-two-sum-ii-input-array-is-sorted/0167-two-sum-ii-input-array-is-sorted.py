class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=1,len(numbers)
        new=[]
        while i<j:
            if numbers[i-1]+numbers[j-1]==target:
                new.append(i)
                new.append(j)
                break
            elif numbers[i-1]+numbers[j-1]>target:
                j-=1
            elif numbers[i-1]+numbers[j-1]<target:
                i+=1
        return new


        