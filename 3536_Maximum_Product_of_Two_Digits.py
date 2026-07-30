n = 431

larg=slarg=0
while n>0:
    digit=n%10
    if digit>larg:
        slarg=larg
        larg=digit
    elif digit>slarg:
        slarg=digit
    n//=10
print(larg)
print(slarg)
print(larg*slarg)