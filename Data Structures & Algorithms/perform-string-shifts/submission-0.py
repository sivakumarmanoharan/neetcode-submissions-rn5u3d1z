class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        '''
        1. For each shift, check whether it is right or left shift. Check shift[0] value 
        2. If left shift(0), s[0] to s[len(s)-1]
        3. If right shift(1), s[len(s)-1] to s[0]
        4. Do the no of shifts from shift[1]
        5. Return the string
        '''
        left, right = 0, len(s)-1
        for sft in shift:
            if sft[0]==0:
                for times in range(sft[1]):
                    s = s[1:]+s[0]
            elif sft[0] == 1:
                for times in range(sft[1]):
                    s = s[-1]+ s[:-1]
        return s