# insertion function
def insert(arr, pos, value):
    shifts = 0
    
    arr.append(0)  # increase size
    
    for i in range(len(arr)-1, pos, -1):
        arr[i] = arr[i-1]
        shifts += 1
    
    arr[pos] = value
    return shifts


# deletion function
def delete(arr, pos):
    shifts = 0
    
    for i in range(pos, len(arr)-1):
        arr[i] = arr[i+1]
        shifts += 1
    
    arr.pop()
    return shifts


# main program
arr = list(map(int, input("Enter elements: ").split()))

print("Array:", arr)

# insertion
pos = int(input("Enter position to insert: "))
val = int(input("Enter value: "))

s = insert(arr, pos, val)
print("After insertion:", arr)
print("Shifts:", s)

# deletion
pos = int(input("Enter position to delete: "))

s = delete(arr, pos)
print("After deletion:", arr)
print("Shifts:", s)
