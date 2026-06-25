jewels = "aA" 
stones = "aAAbbbb"
c=0
for ch in stones:
    if ch in jewels:
            c+=1
print(c)