class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Frequency arrays for characters in s1 and s2 (26 lowercase letters)
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Populate frequency array for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        # Check initial window
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Index of the new character in the window
            right_index = ord(s2[i]) - ord('a')
            left_index = ord(s2[i - len(s1)]) - ord('a')
            
            # Update the right side of the window
            s2_count[right_index] += 1
            if s2_count[right_index] == s1_count[right_index]:
                matches += 1
            elif s2_count[right_index] == s1_count[right_index] + 1:
                matches -= 1
            
            # Update the left side of the window
            s2_count[left_index] -= 1
            if s2_count[left_index] == s1_count[left_index]:
                matches += 1
            elif s2_count[left_index] == s1_count[left_index] - 1:
                matches -= 1
        
        return matches == 26
