class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == ')' or s[0] =='}' or s[0] ==']':
            return False
        par_pairs = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        par_stack = []
        for char in s:
            if char in ('[','(','{'):
                par_stack.append(char)
                continue
            if par_stack and par_pairs[char]==par_stack[-1]:
                par_stack.pop()
            else:
                return False
        return len(par_stack)==0
