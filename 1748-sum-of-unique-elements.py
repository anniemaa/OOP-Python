class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        h = {}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        # print(h) print the count

        result = 0
        for key in h.keys():
            if h[key]==1:
                result+=key
        return result
        """
        n = Counter(nums)
        res = 0
        print(n)
        for i in n:
            if n[i]==1:
                res+=i
        return res
        """
