nums = [2,1,1,2]
j=1
sj=0
while j<len(nums):
    sj=sj+nums[j]
    j+=2
print(sj)
i=0
si=0    
while i < len(nums):
    si=si+nums[i]
    i+=2
print(si)
print(max(si,sj))
