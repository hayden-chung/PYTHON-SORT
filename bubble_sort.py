arr = [10, 5, 7, 22, 30]

while True:
    swap_count = 0
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            temp = arr[i+1]
            arr.pop(i+1)
            arr.insert(i, temp)
            swap_count += 1
    if swap_count == 0:
        print(arr)
        break
