s=[34,12,24,9,67]
for i in range(len(s)):
    mini=i
    for j in range(i+1,len(s)):
        if s[mini]>s[j]:
            mini=j
    s[mini],s[i]=s[i],s[mini]
print(s)