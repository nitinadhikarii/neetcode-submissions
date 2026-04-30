class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        else:
            for i in range(len(nums)+1):
                if i not in nums:
                    return i 
                    break

