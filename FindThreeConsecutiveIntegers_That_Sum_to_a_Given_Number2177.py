num=33
list1=[]
for i in range(num//2):
    if i-1+i+i+1==num:
        list1.append(i-1)
        list1.append(i)
        list1.append(i+1)
print(list1)