s = "aba"
i=0
j=len(s)-1
while i<j:
    if s[i]!=s[j]:
        break
    i+=1
    j-=1
