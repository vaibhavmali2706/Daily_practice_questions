li = "abcde"
goal = "cdeab"
lii=list(li)
gpl=list(goal)

while(lii!=gpl):
    e=lii.pop()
    lii.insert(0, e)
print(lii)