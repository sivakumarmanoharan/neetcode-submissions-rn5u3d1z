class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        1. Initialize pivot_index as -1
        2. Initialize left_sum = 0
        3. Maintain left_sum += nums
        4. For i in range len(nums), if left_sum == right_sum, return i,
        5. Else right_sum = total_sum - left_sum- nums[i]
        '''
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1