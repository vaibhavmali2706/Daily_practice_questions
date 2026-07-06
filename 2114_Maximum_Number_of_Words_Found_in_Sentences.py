s = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
max_words = 0
for i in range(len(s)):
    max_words = max(max_words, len(s[i].split()))
print(max_words)
    