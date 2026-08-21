from collections import Counter
class Solution:
    def divideArray(self, nums):
        if len(nums)%2!=0:
            return False
        count=Counter(nums)
        for val in count.values():
            if val%2!=0:
                return False
        return True

nums = [3,2,3,2,2,2]
s= Solution()
print(s.divideArray(nums))  # Output: True