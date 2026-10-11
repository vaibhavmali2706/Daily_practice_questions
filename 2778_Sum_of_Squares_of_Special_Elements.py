class Solution:
    def sumOfSquares(self, nums):
        n=len(nums)
        special_elements=0
        for i in range(1,n+1):
            if n%i==0:
                special_elements+=nums[i-1]**2
        return special_elements

a=[1,2,3,4]

print(Solution().sumOfSquares(a))
                
        