class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strnum = ""
        for i in digits:
            strnum=strnum+str(i)
        strnum=str(int(strnum)+1)
        answer = []
        for j in strnum:
            answer.append(int(j))
        return answer


        