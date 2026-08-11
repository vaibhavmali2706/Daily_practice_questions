s="0P"
s=s.lower()
i=0
j=len(s)-1
while i<j:
    if not s[i].isalpha():
        i+=1
    elif not s[j].isalpha():
        j-=1
    elif s[i]!=s[j]:
            print(False)
            break
    else:
        i+=1
        j-=1

print(True)