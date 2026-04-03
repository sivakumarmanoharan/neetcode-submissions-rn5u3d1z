class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = dict(Counter(nums))
        for key, value in num_dict.items():
            if value != 1:
                return True
        return False
