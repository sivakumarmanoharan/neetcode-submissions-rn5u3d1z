class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_dict = {0:1}
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            if current_sum-k in count_dict:
                count += count_dict[current_sum-k]
            count_dict[current_sum] = count_dict.get(current_sum,0) + 1
        return count

