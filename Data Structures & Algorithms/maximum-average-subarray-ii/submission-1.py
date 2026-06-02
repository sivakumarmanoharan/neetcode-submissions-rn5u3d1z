class Solution:
    def findMaxAverageFixed(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)
        return max_sum /k  

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avgs = []
        for w in range(k, len(nums)+1):
            avgs.append(self.findMaxAverageFixed(nums, w))
        return max(avgs)