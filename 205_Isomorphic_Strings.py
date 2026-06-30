s = "f11" 
t = "b23"

hps = {}
hpt = {}

for i,j in zip(s,t):
    if i in hps:
        if hps[i] != j:
            print(False)
            break
    else:
        hps[i] = j

    if j in hpt:
        if hpt[j] != i:
            print(False)
            break
    else:
        hpt[j] = i
print(True)