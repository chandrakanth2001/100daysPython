#max element in array

arr = [12,56,784,323,454,575,75778,6553]

def maxInArray(arr):
    max = 0

    for i in range(0,len(arr)):
        if arr[i] > max:
            max = arr[i]
    print(f"Max element in this array is {max}")
maxInArray(arr)