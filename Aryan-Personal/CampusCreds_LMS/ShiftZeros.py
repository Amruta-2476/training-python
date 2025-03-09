mylist = [0, 1, 0, 3, 12]
for i in range(len(mylist)):
    if mylist[i] == 0:
        mylist.append(mylist.pop(i))
    
print(mylist)