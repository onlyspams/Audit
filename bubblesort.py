#bubble sort
array = [3,2,5,6,9,7,1]
n = len(array)
for i in range(n-1):
    for j in range(n-i-1):
        if  array[j] > array[j+1]:
            array[j] ,array[j+1] = array[j+1], array[j]
print("Sorted array:",array)