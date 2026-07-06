nums =[5,6,2,7,4]
smallest = float('inf')
largest = float('-inf')
s_smallest2 = float('inf')
s_largest2 = float('-inf')

for i in range(len(nums)):
    if nums[i] < smallest:
        s_smallest2 = smallest
        smallest = nums[i]
    elif nums[i] < s_smallest2:
        s_smallest2 = nums[i]

    if nums[i] > largest:
        s_largest2 = largest
        largest = nums[i]
    elif nums[i] > s_largest2:
        s_largest2 = nums[i]
print((largest * s_largest2) - (smallest * s_smallest2))
