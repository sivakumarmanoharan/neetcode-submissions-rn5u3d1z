class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        '''
        output = []
        for i in range(len(nums)):
            res = 1
            for index, num in enumerate(nums):
                if index == i:
                    continue
                res *= num
            output.append(res)
        return output