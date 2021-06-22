class Solution:
    def climbStairs(self, n: int) -> int:
        """
        if n==1:
            return n
        oneStep=1
        twoStep=2

        for i in range(3,n+1):
            tmp=twoStep
            twoStep=oneStep+twoStep
            oneStep=tmp
        return twoStep
        """
        if n == 0 or n == 1:
            return n

        # initializes all the n spaces with 0’s
        nums = [0] * (n + 1)
        nums[0] = 1
        nums[1] = 1
        nums[2] = 2
        for i in range(3, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[n]