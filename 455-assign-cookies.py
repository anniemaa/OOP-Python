class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        #opposite direction
        g.sort(reverse = True)
        s.sort(reverse = True)

        i = 0
        j = 0
        contentChildren = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j+=1
                contentChildren+=1 #adding an extra variable for clarity
            i+=1

        return contentChildren
        """

        g.sort()
        s.sort()
        contentChildren = 0
        i = len(g) - 1
        j = len(s) - 1
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                contentChildren += 1
                j -= 1
            i -= 1
        return contentChildren
