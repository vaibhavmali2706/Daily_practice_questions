nums = [4,3,2,7,8,2,3,1]
n = len(nums)
result = {}
for i in range(1, n + 1):
    if i not in nums:
        result[i] = True
print(list(result.keys()))   
