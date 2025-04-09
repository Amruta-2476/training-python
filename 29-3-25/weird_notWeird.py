# conditional weird not weird

n = int(input())

if n%2 != 0:
    print('Weird (odd)')
else:
    if 2 <= n <= 5:
        print('Not Weird (2-5)')
    elif 6 <= n <= 20:
        print('Weird (6-20)')
    else:
        print('Not Weird (>20)')