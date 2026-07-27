s = "leEeetcode"
i=0
stack = []
while i < len(s) :
    if stack and (s[i].lower() == stack[-1].lower()) and s[i] != stack[-1]:
        stack.pop()
    else:
        stack.append(s[i])
    i += 1
print(''.join(stack))