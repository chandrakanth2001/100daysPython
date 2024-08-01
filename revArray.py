#reversing array
# Input - [1,4,45,100,7,5,3,6]
# Output - []

arr = [1,4,45,100,7,5,3,6]

def revArray(arr):
    last_index = len(arr)-1

    newArray = []

    for i in range(len(arr)):
        newArray.append(arr[last_index-i])
    return newArray

print(revArray(arr))