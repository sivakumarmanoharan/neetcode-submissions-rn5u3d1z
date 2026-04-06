class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        '''
        1. Initialize the counter
        2. Find the max number
        3. If the max number is repeated, find the next one
        4. Repeat till you find only one occurence
        5. If nothing found, return -1
        '''
        large_unique_number = -1
        num_dict = dict(Counter(nums))
        nums.sort(reverse=True)
        for num in nums:
            if num_dict[num] == 1:
                large_unique_number = num
                break
        return large_unique_number