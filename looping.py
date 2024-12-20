# for i in range(-11, 0):    # when i is not initialized, it will start from 0
#     print(i)

# for j in range(1, 11, 2):    #print with step 2
#     print(j)

# for j in range(10, 0, -1):    # descending order
#     print(j)

# for j in range(1, 11):    # table of 2
#      print(j*2)


''' Q) how to print this table
2  3  4  5  6  7  8  9  10
4  6  8  10 12 14 16 18 20
6  9  12 15 18 21 24 27 30
8  12 16 20 24 28 32 36 40
10 15 20 25 30 35 40 45 50

11 12 13 14 15 16 17 18 19 20
22 24 26 28 30 32 34 36 38 40
33 36 39 42 45 48 51 54 57 60
44 48 52 56 60 64 68 72 76 80
55 60 65 70 75 80 85 90 95 100
'''
# for i in range(1, 11):
#     for j in range(2, 11):
#            print(i*j, end="\t")
#     print()
    


'''
Q)
1 5
2 4
4 2
5 1
'''
# for i,j in zip(range(1,6), range(5,0,-1)):
#     if i==3 or j==3:
#           continue
#     print(i,j)
for i in range(1, 6):      # i goes from 1 to 5
    j = 6 - i              # Calculate j (5 to 1) based on i
    if i == 3 or j == 3:   # Skip if either i or j equals 3
        continue
    print(i, j)



# Q) wap to accept one character either lower case, upper case or digit or special character and print the type of character
ch = ord(input("enter one character: "))
# ord function is used to convert the character to its ASCII value
if ch>=65 and ch<=91:
    print("upper case")
elif ch>=97 and ch<=122:
    print("lower case")
elif ch>=48 and ch<=57:
    print("digit")
else:
    print("special character")


# Q) wap to print weekday if sat and sun input
day = input("enter day: ")
if day.lower() == "saturday" or day.lower() == "saturday":
    print("weekend")
else:
    print("weekday")