class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_array = []
        for num in nums:
            if num not in set_array:
                set_array.append(num)
        return len(set_array)!=len(nums)