n=28
digits = [int(d) for d in str(n)]
s=1
r=0
for d in digits:
    s=s*d
    r=r+d
print(s-r)