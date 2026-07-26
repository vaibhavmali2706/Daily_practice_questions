nums=[1,2,3]
nums.sort()
p1=nums[-1]*nums[-2]*nums[-3]
p2=nums[0]*nums[1]*nums[-1]
print(max(p1,p2))