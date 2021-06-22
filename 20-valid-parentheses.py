class Solution:
    def isValid(self, s: str) -> bool:
        pastParens = []
        for i in s:
            if self.isOpenParens(i):
                pastParens.append(i)
            elif len(pastParens) == 0:
                return False
            else:
                op = pastParens.pop()
                cl = i
                if not self.parenIsSameType(op, cl):
                    return False
        return len(pastParens) == 0

    def isOpenParens(self, p):
        if p == '(' or p == '[' or p == '{':
            return True
        else:
            return False

    def parenIsSameType(self, op, cl):
        if op == '(' and cl == ')':
            return True
        if op == '[' and cl == ']':
            return True
        if op == '{' and cl == '}':
            return True
        else:
            return False