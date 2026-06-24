nums=[4,7,3,2,6]
numss=list(set(nums))
numss.sort(reverse=True)
if len(numss)>=3:
    print(numss[2]) 
else:
    print(numss[0])