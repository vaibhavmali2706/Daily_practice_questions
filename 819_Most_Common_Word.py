from collections import defaultdict
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
d=defaultdict(int)
simple_str=''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
for word in simple_str.split():
    if word not in banned:
        d[word]+=1
print(max(d,key=d.get))