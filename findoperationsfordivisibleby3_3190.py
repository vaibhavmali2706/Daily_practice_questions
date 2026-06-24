nums = [1,2,3,4]
count=0
for i in range(len(nums)):
    if nums[i]%3==0:
        continue
    elif nums[i]%3-1==0:
        nums[i]=nums[i]+2
        count += 1
    elif nums[i]%3-2==0:
        nums[i]=nums[i]+1
        count += 1 
print(nums) 
print(count)