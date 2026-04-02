class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            index = nums2.index(num)
            res = -1
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    res = nums2[i]
                    break
            ans.append(res)
        return ans