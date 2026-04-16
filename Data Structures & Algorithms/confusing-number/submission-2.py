class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n ==0:
            return False
        original_n = n
        confusing_number_dict = {
            0:0,
            1:1,
            6:9,
            8:8,
            9:6
        }
        rotated_num = 0
        invalid_nums = [2,3,4,5,7]
        while n > 0:
            cur_last_n = n % 10
            if cur_last_n in invalid_nums:
                return False
            rotated_num = rotated_num * 10 + confusing_number_dict[cur_last_n]
            n //=10
        return rotated_num != original_n