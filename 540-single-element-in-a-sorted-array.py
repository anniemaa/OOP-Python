class Solution:

    def singleNonDuplicate(self, nums: List[int]) -> int:

        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
            print(h)
        for key in h.keys():
            if h[key] == 1:
                return key