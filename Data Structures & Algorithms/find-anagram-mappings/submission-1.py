class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        1. Initialize a dictionary
        2. Map the elements in the second array with the indexes corresponding
        3. Use that dictionary to find the elements index and append it
        4. Return the dictionary
        '''
        map_dict = {}
        result = []
        n = len(nums1)
        for i in range(n):
            map_dict[nums2[i]]=i
        for i in range(n):
            result.append(map_dict[nums1[i]])
        return result