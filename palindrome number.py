class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        # Single digit numbers (including 0) are palindromes
        if x < 10:
            return True
        # Numbers ending in 0 are only palindromes if they are 0
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_half = 0
        # Reverse only half of the number
        while x > reversed_half:
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10
        
        # For even-length numbers: x == reversed_half
        # For odd-length numbers: x == reversed_half // 10 (to ignore middle digit)
        return x == reversed_half or x == reversed_half // 10