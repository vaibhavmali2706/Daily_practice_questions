nums = [5,7,7,8,8,10]
target = 8
j=len(nums)-1
for i in range(len(nums)):
    if nums[i]!=target :
        i=i+1
        break
    if nums[j]!=target:
        j=j-1
       
        break
print(i,j)
        
    