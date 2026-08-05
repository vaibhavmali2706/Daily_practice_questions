s = "a"
t = "aa"
e=""
for i in t:
    if i in s:
        s = s.replace(i, "", 1)
    else:
        e += i
print(e)
