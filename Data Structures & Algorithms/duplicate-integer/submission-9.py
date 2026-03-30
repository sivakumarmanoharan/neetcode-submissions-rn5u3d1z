class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_array = set()
        for num in nums:
            if num in set_array:
                return True
            set_array.add(num)
        return False