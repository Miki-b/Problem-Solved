class Solution:
    def reverseVowels(self, s: str) -> str:
        new = list(s)
        vowels = set('aeiouAEIOU')
        left, right = 0, len(s) - 1 

        while left < right:
            if new[left].lower() in vowels and new[right].lower() in vowels:
                new[left], new[right] = new[right], new[left]
                left += 1
                right -= 1
            elif new[left].lower() not in vowels:
                left += 1
            elif new[right].lower() not in vowels:
                right -= 1

        return "".join(new)
