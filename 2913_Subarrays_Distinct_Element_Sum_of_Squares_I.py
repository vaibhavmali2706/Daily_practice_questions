nums = [1,2,1]
class Solution:
    def sumCounts(self, nums):
        tar=0
        for i in range(0,len(nums)):
            seenq=set()
            for j in range(i, len(nums)):
                seenq.add(nums[j])
                r=len(seenq)
                tar+=r*r
        return tar

solution = Solution()
print(solution.sumCounts(nums))
            