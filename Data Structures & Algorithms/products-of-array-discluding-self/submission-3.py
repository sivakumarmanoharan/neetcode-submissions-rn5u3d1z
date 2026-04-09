class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt, prod = 0, 1
        res = [0]* len(nums)
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                prod *=num
        if zero_cnt > 1: 
            return res
        for i,c in enumerate(nums):
            if zero_cnt:
                res[i]=0 if c else prod
            else:
                res[i] = prod//c
        return res
        