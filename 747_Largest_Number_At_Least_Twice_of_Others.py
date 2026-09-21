nums = [3,6,1,0]
class solution:
    def dominantIndex(self, nums):
        max_num = max(nums)
        for num in nums:
            if num != max_num and max_num < 2 * num:
                return -1
        return nums.index(max_num)
s=solution()
print(s.dominantIndex(nums))