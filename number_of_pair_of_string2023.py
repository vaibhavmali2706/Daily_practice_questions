nums=["123","4","12","34"]
target = "1234"
count=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]+nums[j]==target:
            count+=1
print(count)