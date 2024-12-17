name='amrutapawar'
vowel = 0
consonent_count = 0
for i in name:
    # print(i)
    if i in "aeiou":
        vowel+=1
    else:
        consonent_count+=1

print("vowels in ", name , 'are', vowel)
# print("consonents in ", name , 'are', (len(name)-vowel))
print("consonents in ", name , 'are', consonent_count)