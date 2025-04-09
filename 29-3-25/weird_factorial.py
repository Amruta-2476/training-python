# amit has given a number. he decides

# eg : 
'''
IP = 145    => 1!+4!+5!+15 = 1+24+120+15 = 160
OP = 160
'''
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * (fact(num-1))


num = int(input('enter number: '))
total = [15]
while num%10 != 0:
    # print(num%10)
    total.append(fact(num%10))
    num = num//10
print(total)
print(sum(total))