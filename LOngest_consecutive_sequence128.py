nums = [100,4,200,1,3,2]
s=list(set(nums))
s.sort()
mcou=1
cou=1
for i in range(1,len(s)):
    if s[i-1]+1==s[i]:
        cou+=1
        mcou=max(mcou,cou)
    else:
        cou=1
print(mcou)