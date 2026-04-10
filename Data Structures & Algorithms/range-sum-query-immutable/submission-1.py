class NumArray:

    def __init__(self, nums: List[int]):
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        self.prefix_sum = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right]-self.prefix_sum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)