strs = ["eat","tea","tan","ate","nat","bat"]
hp={}
if not strs:
    print ([[""]])
for s in strs:
    a=''.join(sorted(s))

    if a in hp:
        hp[a].append(s)

    else:
        hp[a]=[s]
print(list(hp.values()))