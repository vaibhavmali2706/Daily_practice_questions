class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([i**2 for i in nums])
l=[-4,-1,0,3,10]
solution = Solution()  
print(solution.sortedSquares(l))