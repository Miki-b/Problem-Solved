class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Base case: if the string is empty or has only one character, return empty string
        if len(s) < 2:
            return ""
        
        # Check if every character has its uppercase and lowercase forms in the string
        for i in range(len(s)):
            if s[i].swapcase() not in s:
                # Recursively check the left and right substrings split by this character
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                
                # Return the longer nice substring of the two
                return left if len(left) >= len(right) else right
        
        # If all characters have their counterparts, the whole string is nice
        return s
