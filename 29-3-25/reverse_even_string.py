s = input('enter string: ')
s = s.split()
print(s)

rev_words = []
for i in range(len(s)):
    if i%2 != 0:
        rev_words.append(s[i][::-1])
print(rev_words)

index = 0
for i in range(len(s)):
    if i%2 != 0:
        s[i] = rev_words[index]
        index = index + 1
print(s)
print(' '.join([str(i) for i in s]))




'''
better =>
'''
s = input('enter string: ')
s = s.split()
print(s)
for i in range(len(s)):
    if i%2 != 0:
        s[i] = s[i][::-1]
print(' '.join(s))