class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = dict(Counter(nums))
        for val in num_dict.values():
            if val!=1:
                return True
        return False
