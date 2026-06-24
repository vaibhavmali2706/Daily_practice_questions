nums = [2,0,2,1,1,0]

i=0
j=len(nums)-1
m=0
while m <=j:
    if nums[m]==0:
        nums[m],nums[i]=nums[i],nums[m]
        i+=1
        m+=1
    elif nums[m]==1:
        m+=1
    elif nums[m]==2:
        nums[m],nums[j]=nums[j],nums[m]
        
        j-=1
        
print(nums)
    