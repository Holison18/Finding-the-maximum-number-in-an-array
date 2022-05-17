arr = [1,28,48,33,45,23,89,4,56,92,15]
max = arr[0]
for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]
print("The maximum value is",max)