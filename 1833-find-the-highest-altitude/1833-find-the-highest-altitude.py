class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum=0
        answer=0
        print(answer)
        for i in range(len(gain)):
            sum+=gain[i]
            answer=max(answer,sum)
        return answer
        