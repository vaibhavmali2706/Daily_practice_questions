nums = [1,2,-2147483648]
nums.sort()
fl=0
sl=0
tl=0
for i in nums:
    if i>fl:
        tl=sl
        sl=fl
        fl=i
if tl==0:
    tl=fl
print(fl)
print(sl)   
print(tl)