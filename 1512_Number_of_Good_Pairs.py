class Solution:
    def numIdenticalPairs(self, nums):

        count = {}
        ans = 0

        for num in nums:
            ans += count.get(num, 0)
            count[num] = count.get(num, 0) + 1

        return ans
sol=Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))