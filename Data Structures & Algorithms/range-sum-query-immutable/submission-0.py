class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sub_array = self.nums[left:right + 1]
        return sum(sub_array)
