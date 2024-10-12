class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()  # Sort the list in ascending order
        n = len(piles)
        count = 0
        i = n - 2  # Start from the second last element
        res = 0
        while count != n // 3:
            res += piles[i]  # Add the second largest number in each step
            i -= 2  # Move two steps back to skip the smallest and pick the next second largest
            count += 1  # Increment count after picking one for you

        return res