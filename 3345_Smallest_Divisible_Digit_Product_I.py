n = 15
t = 3
def digip(n):
    x=1
    while n>0:
        a=n%10
        x *= a
        n //= 10
    return x
while True:
    if digip(n)%t==0:
        print(n)
        break
    n+=1