class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total_sum = max_sum = 0
        for i in nums:
            if i==0:
                total_sum=0
            elif i==1:
                total_sum+=1
                max_sum=max(max_sum,total_sum)
                #print(max_sum)
        return max_sum