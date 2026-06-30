word = "aba"

vowels = "aeiou"
c=0
n=len(word)
for i in range(n):
    if word[i] in vowels:
        c+=(i+1)*(n-i)
print(c)