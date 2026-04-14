class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        1. Initialize a final array
        2. If nums1 not in nums2, remove the common elements and append in final array
        3. Do step 2 for nums2 with respect to nums1
        '''
        final_array = []
        step_array = []
        for i in set(nums1):
            if i not in nums2:
                step_array.append(i)
        final_array.append(step_array)
        
        step_array = []
        for i in set(nums2):
            if i not in nums1:
                step_array.append(i)
        final_array.append(step_array)
        
        return final_array