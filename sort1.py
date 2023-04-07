arr = [10, 5, 7, 22, 30]

for i in range(len(arr)):
    min = i
    for k in range(i, len(arr)):
        if arr[k] < arr[min]:
            min = k
    temp = arr[min]
    arr.pop(min)
    arr.insert(i, temp)

print(arr)