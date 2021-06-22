class Solution:
    """
    :type nums:list[int]
    :type target: int

    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = l+(r-l)//2
            if (nums[mid] == target):
                return mid
            elif (nums[mid]<target):
                l = mid+1
            else:
                h = mid-1
        return l


    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


    def searchInsert(self, nums, target):
        index = 0
        if not nums:
            return 0
        while index < len(nums):
            if target > nums[index]:
                index += 1
            else:
                return index
        return len(nums)

    """