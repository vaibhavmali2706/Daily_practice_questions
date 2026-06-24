num =526
tar=0
tar2=0
while(num>=1):
    digit=num%10
    tar=int(tar*10+digit)
    num=num/10
while(tar>=1):
    digit=tar%10
    tar2=int(tar2*10+digit)
    tar=tar/10
if num==tar2:
    print("true")
print(tar2)