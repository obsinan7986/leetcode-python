class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Total numbers in the range (inclusive)
        count = high - low + 1
        # If both low and high are odd, add 1 to the count before dividing
        if low % 2 == 1 and high % 2 == 1:
            return (count + 1) // 2
        # Otherwise, just divide the count by 2
        return count // 2
        