class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        running_sum = 0
        rem_hm = {0:-1}
        for i, num in enumerate(nums):
            running_sum += num 
            remainder = running_sum % k
            if remainder in rem_hm:
                if i-rem_hm[remainder] >= 2:
                    return True
            else:
                rem_hm[remainder] = i
        return False
