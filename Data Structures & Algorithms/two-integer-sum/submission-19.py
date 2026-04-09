class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        1. Create a diff hashmap
        2. For i=0 to len(nums), you need to store the index
        3. Find the difference between current number and target
        4. If the number is present in diff hashmap, return the index from the diff hashmap and current index
        '''

        diff_hashmap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in diff_hashmap:
                return [diff_hashmap[diff], index]
            diff_hashmap[num]=index