# def search(data,key,min,max):
#     mid = int((min + max) / 2)
#     if data[mid] == key:
#         return mid
#     elif data[mid] > key:
#         max = mid -1
#         return search(data, key, min, max)
#     else:
#         min = mid + 1
#         return search(data, key, min, max)


def search2(data, key):
    min = 0
    max = len(data) - 1

    while max >= min:
        mid = int((min+max) / 2)
        if data[mid] == key :
            return mid
        elif data[mid] > key :
            max = mid - 1
        else:
            min = mid + 1



data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 7

# print(search(data,7,0,len(data)-1))

print( search2(data, key))