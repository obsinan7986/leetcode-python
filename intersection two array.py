from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_map = defaultdict(int)
        result = []
        for num in nums1:
            count_map[num] += 1
        
        for num in nums2:
            if count_map[num] > 0:
                result.append(num)
                count_map[num] -= 1
        
        return result