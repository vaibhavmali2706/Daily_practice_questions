li=[1,2,3,4,5]
k=2
n=len(li)
l=k%n
"""for _ in range(l):
    e=li.pop()
    li.insert(0, e)
print(li)"""

li[:]=li[n-l:]+li[:n-l]
print(li)