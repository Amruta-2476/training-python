# match case is basically switch case
value = 2
match value:
    case 1:
        print('one')
    case 2:
        print('two')
    case 3:
        print('three')
    case 4:
        print('four')


value = int(input())
match value:
    case 1|2|3|4:
        print('one')
    case 5|6|7|8:
        print('two')
    case 9|10:
        print('three')
    case default:     # or case _: 
        print('lol')



# list or tuple in match case, can also use dictionary....cannot use float as case i guess (check)

# x,y = map(int, input().split())
# print(x,y)
# print(type(x),type(y))
li = list(map(int, input().split()))
print(li)

match li:
    case [0,0]:
        print('origin')
    case (x,0):              # can check case using tuple as well even tho we took it as list
        print(f'X-axis at {x}')
    case [0,y]:
        print(f'Y-axis at {y}')
    case [x,y]:
        print(f'Point at ({x},{y})')
    



di = eval(input())
print(di, type(di))

match di:
    case {'a':l, 'b':m, 'c':n}:
        print(f'this is a dictionary. a={l}, b={m}, c={n}')
    case {'x':l, 'y':m, 'z':n}:
        print(f'this is a dictionary. x={l}, y={m}, z={n}')




per = 30
match per:
    case per if per%3==0:       # when a case matches, then it will not go to the next phase, even if next caase also satisfies
        print('hi there 3')
    case per if per%2==0:      # case per%2==0:       is not allowed. syntaxerror
        print('hi there again 2')
    case _:
        print('byee')