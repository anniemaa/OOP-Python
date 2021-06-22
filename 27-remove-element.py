class Solution:
    """
    :type nums:List[int]
    :type val:int

    def removeElement(self, nums, val):
        index = 0
        for i in nums:
            if i!= val:
                nums[index] = i
                index += 1
        return index
    """

    def removeElement(self, nums, val):
        index = 0
        for i in nums:
            if i != val:
                nums[index] = i
                index += 1
        return index