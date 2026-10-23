from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0

        for num in nums:
            total = total + num
            result.append(total)

        return result
s = Solution()
print(s.runningSum([2, 5, 1]))