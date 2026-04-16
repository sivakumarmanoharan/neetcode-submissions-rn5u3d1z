class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n ==0:
            return False
        confusing_number_dict = {
            0:0,
            1:1,
            6:9,
            8:8,
            9:6
        }
        rotated_num = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            temp //= 10
            if digit not in confusing_number_dict:
                return False
            rotated_num = rotated_num * 10 + confusing_number_dict[digit]
        return rotated_num != n