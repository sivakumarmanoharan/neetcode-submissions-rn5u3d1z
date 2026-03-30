class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            ans.append([num,i])
        ans.sort()

        i, j = 0, len(nums)-1
        while i < j:
            cur = ans[i][0] + ans[j][0]
            if cur == target:
                return [min(ans[i][1], ans[j][1]), max(ans[i][1], ans[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return[]            