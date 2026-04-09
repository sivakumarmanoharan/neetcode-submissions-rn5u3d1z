class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        1. Initialize count = 0
        2. Use a hash map to store the frequency of prefix sums
        3. Iterate through the array once (O(n))
        4. Return count
        '''
        count = 0
        n = len(nums)
        prefix_sums = {0: 1}
        current_sum = 0
        for i in range(n):
            current_sum += nums[i]
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        return count
