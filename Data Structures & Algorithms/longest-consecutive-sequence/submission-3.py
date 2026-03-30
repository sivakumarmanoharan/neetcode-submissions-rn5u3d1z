class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset =list(set(sorted(nums)))
        longest = 0
        if len(nums) == 0:
            return 0
        for i in numset:
            if i-1 not in numset:
                length = 1
                while (i+length) in numset:
                    length += 1
                longest = max(length,longest)
        return longest