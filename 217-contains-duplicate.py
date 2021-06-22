class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                return True
        return False
        """
        numsSet =  set(nums)
        if len(nums) == len(numsSet):
            return False
        return True