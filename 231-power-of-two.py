class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        return n > 0 and not (n & n-1)
        """
        i = 1
        while(i<n):
            i*=2
        return i==n