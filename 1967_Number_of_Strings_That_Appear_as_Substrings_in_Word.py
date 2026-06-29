patterns = ["a","abc","bc","d"]
word = "abc"
c=0
for i in patterns:
    if i in word:
        c+=1
print(c)