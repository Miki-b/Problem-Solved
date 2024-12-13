class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alphabet="abcdefghijklmnopqrstuvwxyz"
        suffix=0
        new=[_ for _ in s]
        print(new)
        for i in range(len(new)-1,-1,-1):
            
            suffix+=shifts[i]

            new[i]=alphabet[(alphabet.index(new[i])+suffix)%len(alphabet)]
        return ''.join(new)


        