s=["v","s","m"]
k=0
i=len(s)-1
while k<=i:
    s[k],s[i]=s[i],s[k]
    k+=1
    i-=1
print(s)