class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        1. Initialize a map array
        2. For i in nums1, if i in nums2, find the index and append it in the map_array
        3. Return the o/p array
        '''

        map_array = []
        for num in nums1:
            if num in nums2:
                index = nums2.index(num)
                map_array.append(index)
        return map_array