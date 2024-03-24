class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = "qwertyuiopQWERTYUIOP"
        secondRow = "asdfghjklASDFGHJKL"
        thirdRow = "zxcvbnmZXCVBNM"
        answer=[]
       
        for i in range(1,len(words)+1):
            row1=0
            row2=0
            row3=0
            for letter in words[i-1]:
                if letter in firstRow:
                    row1=row1+1
                elif letter in secondRow:
                    row2=row2+1
                elif letter in thirdRow:
                    row3=row3+1
            if row1==0 and row2==0 or row1==0 and row3==0 or row2==0 and row3==0:
                answer.append(words[i-1])
        return answer

    
        