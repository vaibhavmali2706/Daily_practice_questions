nums = [2,7,9]
original = 2
class solution:
    def multiply(self, nums, original):
        while original in nums:
            original *= 2
        return original
s=solution()
print(s.multiply(nums, original))
    
