s=s = "erase*****"
stack = []
for c in s:
    if c == '*':
        stack.pop()
        
    else:
        stack.append(c)
print(''.join(stack))