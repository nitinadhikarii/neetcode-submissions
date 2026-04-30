class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for g in range(0,(len(nums))):
                if nums[g]+ nums[i] == target and i!=g:
                        return [i,g]
                