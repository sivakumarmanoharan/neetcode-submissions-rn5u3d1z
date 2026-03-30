class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_square_digits(n)

        return n == 1
    
    def sum_square_digits(self,n):
        sum=0
        while n > 0:
            digit = n % 10
            sum += digit * digit
            n//=10
        return sum
