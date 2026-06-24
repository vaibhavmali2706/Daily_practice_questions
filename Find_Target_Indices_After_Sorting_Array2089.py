nums = [1,2,5,2,3]
target = 2
a=[]
nums.sort()
for i in range(len(nums)):
    if nums[i]==target:
        a.append(i)
print(a)