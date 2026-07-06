nums = [1,5,4,5]
largest = float('-inf')
s_largest2 = float('-inf')

for i in range(len(nums)):
    if nums[i] > largest:
        s_largest2 = largest
        largest = nums[i]
    elif nums[i] > s_largest2:
        s_largest2 = nums[i]

print((largest-1) * (s_largest2-1))