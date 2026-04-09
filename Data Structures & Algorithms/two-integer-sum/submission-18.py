class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        1. Initialize i=0, j = i+1
        2. Zip the array into a tuple with index and number
        3. While i < j, if arr[i][0]+arr[j][0]==target, return [arr[i][1], arr[j][1]]
        '''
        ans = []
        for index, num in enumerate(nums):
            ans.append([num, index])
        ans.sort()

        i, j = 0, len(nums)-1
        while i < j:
            if ans[i][0]+ ans[j][0] == target:
                return [min(ans[i][1], ans[j][1]), max(ans[i][1], ans[j][1])]
            elif ans[i][0] + ans[j][0] > target:
                j-=1
            else:
                i+=1
        