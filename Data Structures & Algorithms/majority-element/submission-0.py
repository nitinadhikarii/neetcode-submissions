class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm={}
        for i in range(len(nums)):
            if nums[i] not in hm.keys():
                hm[nums[i]]=1
            else:
                hm[nums[i]] +=1  

        for i in hm.keys():
            if hm[i]>((len(nums))/2):
                return i