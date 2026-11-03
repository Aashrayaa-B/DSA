arr = [4, 2, 4, 1]

for passes in range(len(arr) - 1):
    for i in range(len(arr) - 1 - passes):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(arr)
