class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=s.split()
        n=len(word)-1
        return len(word[n])