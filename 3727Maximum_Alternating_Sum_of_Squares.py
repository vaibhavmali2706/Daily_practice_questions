class Solution:
    def maxAlternatingSum(self, nums):
        n=len(nums)
        ans=0
        l=[0]*n
        for i in range(n):
            l[i]=nums[i]*nums[i]
        l.sort()
        mid=n//2
        for i in range (mid):
            ans-=l[i]
        for i in range(mid,n):
            ans+=l[i]
        return ans
solution = Solution()
print(solution.maxAlternatingSum( [1,2,3]))

        
            