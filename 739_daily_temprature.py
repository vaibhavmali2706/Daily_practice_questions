temperatures = [30,40,50,60]
n1=len(temperatures)
res=[0]*n1
stack=[]
for i,n in enumerate(temperatures):
    while stack and temperatures[stack[-1]]<n:
        idx=stack.pop()
        res[idx]=i-idx
    stack.append(i)
print(res)      