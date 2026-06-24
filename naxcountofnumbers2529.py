nums = [-3,-2,-1,0,0,1,2]
ncount = 0
pcount = 0
for num in nums:
    if num < 0:
        ncount += 1
    elif num > 0:
        pcount += 1

print(max(ncount, pcount))