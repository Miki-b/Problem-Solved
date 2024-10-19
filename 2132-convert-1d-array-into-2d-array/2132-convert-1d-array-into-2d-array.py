class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        o = len(original)
        if o != m * n:
            return []
        
        res = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(o):
            res[i // n][i % n] = original[i]
        
        return res