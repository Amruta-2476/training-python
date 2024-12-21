myTuple1 = 1,2
myTuple2 = (3,4)
[print(sum(x)) for x in [myTuple1 + myTuple2]]     # 10


init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)
print(result)    # 6


l = [1,2,3]
init_tuple = ('Python',)*(l.__len__() - l[::-1][0])    # ('Python',)*(3 - 3)  = ('Python',)*0
print(init_tuple)      # ()
# __len__() is same as len()

## beware of the comma ('Python',)


init_tuple = ('Python')*3
print(type(init_tuple))     # <class 'str'>   



init_tuple = ((1,2),)*7
print(init_tuple[3:8])     # ((1, 2), (1, 2), (1, 2), (1, 2))
print(len(init_tuple[3:8]))   # 4


