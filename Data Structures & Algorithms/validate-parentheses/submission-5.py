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
            if char in par_pairs.values():
                par_stack.append(char)
            else:
                if not par_stack:
                    return False
                if par_pairs[char] != par_stack[-1]:
                    return False
                par_stack.pop()
        return len(par_stack)==0
