nums = [2,3,-1,8,4]
class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        ts = sum(nums)
        ls = 0
        
        for i in range(len(nums)):
            rs = ts - ls - nums[i]
            if ls == rs:
                return i
            ls += nums[i]
        
        return -1
print(Solution().findMiddleIndex(nums))