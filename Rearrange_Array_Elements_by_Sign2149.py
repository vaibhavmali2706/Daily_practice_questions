nums = [3,1,-2,-5,2,-4]
res=[0]*len(nums)
pos=0   
neg=1
for i in range(len(nums)): 
    if nums[i]>0: 
        res[pos]=nums[i] 
        pos+=2
    else: 
        res[neg]=nums[i] 
        neg+=2  
print(res)