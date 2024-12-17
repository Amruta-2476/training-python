s =  'amruta'
# for i in range(len(s)-1, -1, -1):
#     print(s[i], end="")

for i in range(1, int(len(s)/2)):
    for j in range(len(s)-1, int(len(s)/2), -1):
        temp = i
        i = j
        j = temp
print(s)


