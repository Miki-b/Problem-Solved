class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word1=word.split()
        ans=[]
        for i in range(len(word)):
            if word[i]==ch:
                ans=word[i::-1]
                print(ans)
                break
        i+=1
        ans+=word[i:]
        if ans:
            return ans
        else:
            return word
