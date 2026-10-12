class Solution:
    def findIndices(self, nums, indexDifference, valueDifference):
        if (indexDifference <= 0 or valueDifference <= 0):
            return [-1, -1]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
solution = Solution()
nums = [5,1,4,1]
indexDifference = 2
valueDifference = 4
print(solution.findIndices(nums, indexDifference, valueDifference))