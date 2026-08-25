nums = [8,3,4,6]
k = 2
class Solution:
    def missingMultiple(self, nums,k) -> int:
        seen = set(nums)
        ans=k
        while ans in seen:
            ans+=k
            
        return ans
        
s=Solution()
print(s.missingMultiple(nums,k))    
    
    
    
