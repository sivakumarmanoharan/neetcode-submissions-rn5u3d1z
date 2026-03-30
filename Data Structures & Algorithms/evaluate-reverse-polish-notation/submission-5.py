class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eqn_stack = []
        for i in tokens:
            if i =='+' :
                fn=eqn_stack.pop()
                sn=eqn_stack.pop()
                result= sn +fn
                eqn_stack.append(result)
            elif i =='-':
                fn=eqn_stack.pop()
                sn=eqn_stack.pop()
                result= sn-fn
                eqn_stack.append(result)
            elif i =='*':
                fn=eqn_stack.pop()
                sn=eqn_stack.pop()
                result= sn*fn
                eqn_stack.append(result)
            elif i =='/':
                fn=eqn_stack.pop()
                sn=eqn_stack.pop()
                result= float(sn)/fn
                eqn_stack.append(int(result))
            else:
                eqn_stack.append(int(i))
        return int(eqn_stack[0])
