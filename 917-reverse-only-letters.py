class Solution:

    def reverseOnlyLetters(self, S: str) -> str:
        S = list(s)
        i = 0
        j = len(S) - 1
        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha():
                j -= 1
            else:
                tmp = S[i]
                S[i] = S[j]
                i += 1
                S[j] = tmp
                j -= 1
        return ''.join(S)