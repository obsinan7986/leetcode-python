class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:  # While num has more than one digit
            temp = 0
            while num > 0:  # Extract and sum digits
                temp += num % 10
                num //= 10
            num = temp  # Update num with the sum
        return num