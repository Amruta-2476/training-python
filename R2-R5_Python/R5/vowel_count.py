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
print("consonents in ", name , 'are', consonent_count)






# name = 'amrutapawar'
# vowel_count = 0
# for i in name:
#     if i in "aeiou":
#         vowel_count +=1
#     else:
#         continue
# print('vowels: ', vowel_count)
# print('consonents: ', (len(name)-vowel_count))