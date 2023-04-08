arr = [10, 5, 7, 22, 30]
output = []

# for i in range(len(input)):
#     min = 9999
#     for j in range(i, len(input)):
#         if input[j] < min:
#             min = input[j]
#         print(output)
#     output.append(min)
# print(output)

min = 123013
min_idx = None
for headidx, item in enumerate(arr):
    if item < min: 
        min = item
        min_idx = idx

print(min, min_idx)

head_idx = 0
temp = arr[head_idx]
arr[head_idx] = min
arr[idx] = temp