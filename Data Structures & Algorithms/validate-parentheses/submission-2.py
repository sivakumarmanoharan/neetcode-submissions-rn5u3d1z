class Solution:
    def isValid(self, s: str) -> bool:
        if s[0]==')' or s[0]=='}' or s[0]==']':
            return False
        parantheses={
            ')':'(',
            '}':'{',
            ']':'['
        }
        par_stack=[]
        for i in s:
            if i in ('(','{','['):
                par_stack.append(i)
                continue
            if par_stack and parantheses[i]==par_stack[-1]:
                par_stack.pop()
            else:
                return False
        return len(par_stack)==0            