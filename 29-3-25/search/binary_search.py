def binary_search(key,list):
    low = 0
    high = len(list) - 1
    while low<= high:
        mid = low + (high - low)//2
        if list[mid] == key:
            return mid
        elif list[mid] > key:
            high = mid - 1
        else:
            low = mid +1    
    return -1
            
key = int(input('enter key: '))
print(binary_search(key, [2,3,5,6,8,9,12,28,44]))