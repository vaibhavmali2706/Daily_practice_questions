word = "abcdefd"
ch = "d"
i = 0
while i < len(word) and word[i] != ch:
    i += 1
if i < len(word):
    word = word[:i+1][::-1] + word[i+1:]
print(word)
