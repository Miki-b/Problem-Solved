class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        ans=0
        if numOnes>k:
            ans=k
            return ans
        else:
            ans+=numOnes
            if k-ans<numZeros:
                return ans
            else:
                
                if( (k-(ans+numZeros))<numNegOnes):
                    print(k)
                    print(k-(ans+numZeros))
                    for i in range((k-(ans+numZeros))):
                        ans+=-1
                    return ans
                else:
                    for _ in range(numNegOnes):
                        ans+=-1
                    return ans


        