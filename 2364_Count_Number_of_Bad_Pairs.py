nums = [4,1,3,3]
n=len(nums)
total_pair=n*(n-1)//2
good=0
hp={}
for i in range(len(nums)):
    value=nums[i]-i
    if value in hp:
        good+=hp[value]
    hp[value]=hp.get(value,0)+1
print(total_pair-good)