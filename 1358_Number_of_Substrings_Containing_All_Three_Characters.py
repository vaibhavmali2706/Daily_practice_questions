s="abcabc"
hp = {'a': 0, 'b': 0, 'c': 0}

left = 0
count = 0

for right in range(len(s)):

    hp[s[right]] += 1

    while hp['a'] > 0 and hp['b'] > 0 and hp['c'] > 0:

        count += len(s) - right

        hp[s[left]] -= 1
        left += 1

print(count)