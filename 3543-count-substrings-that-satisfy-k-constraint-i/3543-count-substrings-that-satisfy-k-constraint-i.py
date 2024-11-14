class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            bin_count = {0: 0, 1: 0}  # Initialize the count for '0' and '1'
            for j in range(i, n):
                bin_count[int(s[j])] += 1  # Update the count for '0' or '1'
                if bin_count[0] <= k or bin_count[1] <= k:  # Check the constraint
                    ans += 1
                else:
                    break  # Stop counting if the constraint is violated
        return ans
