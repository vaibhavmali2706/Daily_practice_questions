s = "aba"
i=0
flag=0
j=len(s)-1
while i<j:
    if s[i] != s[j]:
        flag = 1
        break
    i += 1
    j -= 1

if flag == 0:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")