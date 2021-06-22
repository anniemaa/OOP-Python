class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            i+=1
            s[j]=tmp
            j-=1