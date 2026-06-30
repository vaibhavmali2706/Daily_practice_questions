pattern = "abba"
s = "dog dog dog dog"
s = s.split(" ")
hpa = {}
hpb = {}
     
for p, w in zip(pattern, s):
    if p in hpa:

        if hpa[p] != w:
            print(False)
            break
    else:
        hpa[p] = w  

    if w in hpb:

        if hpb[w] != p:
            print(False)
            break

    else:
        hpb[w]=p

print(True)