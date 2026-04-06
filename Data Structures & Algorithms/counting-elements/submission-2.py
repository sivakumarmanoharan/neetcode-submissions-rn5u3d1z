class Solution:
    def countElements(self, arr: List[int]) -> int:
        '''
        1. Initialize count to 0
        2. For num in arr, if num+1 in arr, count+1
        3. Return count
        '''
        count = 0
        values =set(arr)
        for num in arr:
            if num+1 in values:
                count+=1
        return count