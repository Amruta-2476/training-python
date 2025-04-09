# compare key with each element one by ne
def linear_search(list, key):
    for i in range(len(list)):
        if key == list[i]:
            print(f'key {key} found at index {i}')
            break

key = int(input('enter key to search: '))
li = [100, 50, 30, 70, 80, 60, 20, 90, 40]
linear_search(li,key)