import statistics
nums1 = [1,2]
nums2 = [3,4]

nums=nums1+nums2
nums.sort()
n = len(nums)

if n % 2 == 0:
    median = (nums[n//2] + nums[n//2 - 1]) / 2
else:
    median = nums[n//2]
print(median)

print(statistics.median(sorted(nums1 + nums2)))