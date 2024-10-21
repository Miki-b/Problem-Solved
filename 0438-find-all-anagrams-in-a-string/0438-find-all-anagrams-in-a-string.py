class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = {}  # Frequency map for characters in p
        L = 0  # Left pointer of the window
        ans = []  # Result list for start indices
        sum_matching_chars = 0  # Tracks the number of matching chars in the current window
        
        # Initialize the frequency map for string p
        for char in p:
            if char in anagrams:
                anagrams[char] += 1
            else:
                anagrams[char] = 1
        
        # Copy of the frequency map for the sliding window
        window_count = {char: 0 for char in p}
        
        # Sliding window
        for R in range(len(s)):
            # Add current character to the window if it exists in p
            if s[R] in anagrams:
                window_count[s[R]] += 1
                
                # If the count in the window is less than or equal to the count in p,
                # it means it's still a valid match
                if window_count[s[R]] <= anagrams[s[R]]:
                    sum_matching_chars += 1
            
            # Once the window size matches the size of p, we check for an anagram
            if R - L + 1 == len(p):
                if sum_matching_chars == len(p):  # If all characters match, add the start index
                    ans.append(L)
                
                # Now move the left pointer of the window
                if s[L] in anagrams:
                    # If we are removing a matching character from the window
                    if window_count[s[L]] <= anagrams[s[L]]:
                        sum_matching_chars -= 1
                    window_count[s[L]] -= 1
                
                L += 1  # Slide the window to the right
        
        return ans
