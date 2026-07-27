s = "abc12"
stack = []
i=0
while i < len(s):
    if s[i].isdigit():
        stack.pop()
    else:
        stack.append(s[i])
    i += 1
print(''.join(stack))