nums = [1,2,2,1,1,0]
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        nums[i+1]=0
        nums[i]=2*nums[i]
print(nums)