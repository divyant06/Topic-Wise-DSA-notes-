#Sorting
#Sorting is the process of arranging data in a specific order, such as ascending or descending.
#In Python, you can sort lists using the built-in `sorted()` function or the `list.sort()` method.
#Using `sorted()` function
#The `sorted()` function returns a new sorted list from the items in an iterable.
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)
#Using `list.sort()` method
#The `list.sort()` method sorts the list in place and returns `None`.
numbers.sort()
print("Numbers after sorting:", numbers)
#Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Sorted numbers in descending order:", sorted_numbers_desc)
#Sorting strings
fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits)
print("Sorted fruits:", sorted_fruits)
#Sorting with a custom key
#You can also sort using a custom key function. For example, to sort by the length of the strings:
sorted_fruits_by_length = sorted(fruits, key=len)
print("Fruits sorted by length:", sorted_fruits_by_length)
#Sorting a list of dictionaries
#You can sort a list of dictionaries by a specific key. For example, if you have a list of people with their ages:
people = [
    {"name": "Alice", "age": 30},   
    {"name": "Bob", "age": 25},   
    {"name": "Charlie", "age": 35}
]
#You can sort the list of people by age:        
sorted_people = sorted(people, key=lambda x: x["age"])
print("People sorted by age:", sorted_people)
#Sorting a list of tuples
#You can also sort a list of tuples. For example, if you have a list of tuples representing (name, age):
people_tuples = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
#You can sort the list of tuples by age (the second element of the tuple):
sorted_people_tuples = sorted(people_tuples, key=lambda x: x[1])
print("People tuples sorted by age:", sorted_people_tuples)
#Sorting with multiple criteria
#You can sort with multiple criteria by providing a tuple as the key. For example, if you want to sort by age and then by name:
sorted_people_multi = sorted(people, key=lambda x: (x["age"], x["name"]))
print("People sorted by age and then by name:", sorted_people_multi)
#Sorting in reverse order
#You can sort in reverse order by setting the `reverse` parameter to `True`:
sorted_people_reverse = sorted(people, key=lambda x: x["age"], reverse=True)
print("People sorted by age in reverse order:", sorted_people_reverse)
#Sorting with case-insensitivity
#You can sort strings in a case-insensitive manner by using the `str.lower` method as the key:
sorted_fruits_case_insensitive = sorted(fruits, key=str.lower)
print("Fruits sorted case-insensitively:", sorted_fruits_case_insensitive)
#Sorting with a custom comparison function
#In Python 3, you cannot directly use a custom comparison function for sorting. However, you can achieve similar results by using the `functools.cmp_to_key` function to convert a comparison function into a key function.
from functools import cmp_to_key
def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0
sorted_numbers_custom = sorted(numbers, key=cmp_to_key(compare))
print("Numbers sorted with custom comparison function:", sorted_numbers_custom)
#Bubble Sort
#Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps  them if they are in the wrong order. The process is repeated until the list is sorted.  Here is an implementation of the Bubble Sort algorithm in Python:
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted numbers using Bubble Sort:", sorted_numbers)
#Selection Sort
#Selection Sort is a simple sorting algorithm that divides the input list into two parts: the sorted part and the unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the end of the sorted part. Here is an implementation of the Selection Sort algorithm in Python:
def selection_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Find the minimum element in the unsorted part
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
# Example usage
numbers = [64, 25, 12, 22, 11]  
sorted_numbers = selection_sort(numbers)
print("Sorted numbers using Selection Sort:", sorted_numbers)
#Insertion Sort
#Insertion Sort is a simple sorting algorithm that builds the sorted array one item at a time.  It repeatedly takes the next item from the input and inserts it into the correct position in the already sorted part of the array. Here is an implementation of the Insertion Sort algorithm in Python:
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# Example usage
numbers = [12, 11, 13, 5, 6]
sorted_numbers = insertion_sort(numbers)
print("Sorted numbers using Insertion Sort:", sorted_numbers)
#Merge Sort
#Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves,
#sorts each half recursively, and then merges the sorted halves back together. Here is an implementation of  the Merge Sort algorithm in Python:
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
# Example usage
numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_numbers = merge_sort(numbers)
print("Sorted numbers using Merge Sort:", sorted_numbers)
#Quick Sort
#Quick Sort is a divide-and-conquer algorithm that selects a 'pivot' element from the array and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. Here is an implementation of the Quick Sort algorithm in Python:
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# Example usage
numbers = [3, 6, 8, 10, 1, 2   , 1]
sorted_numbers = quick_sort(numbers)
print("Sorted numbers using Quick Sort:", sorted_numbers)
#Heap Sort
#Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements
#in place. The algorithm first builds a max heap from the input data, and then repeatedly extracts the maximum element from the heap and rebuilds the heap until it is empty. Here is an implementation of the Heap Sort algorithm in Python:
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr
# Example usage
numbers = [12, 11, 13, 5, 6, 7  ]
sorted_numbers = heap_sort(numbers)
print("Sorted numbers using Heap Sort:", sorted_numbers)
#Counting Sort
#Counting Sort is a non-comparison-based sorting algorithm that sorts integers by counting the number of occurrences of each unique element in the input array. The count is stored in an auxiliary array, and the sorted output is generated by iterating through the count array. Here is an implementation of the Counting Sort algorithm in Python:
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i, c in enumerate(count):
        sorted_arr.extend([i] * c)
    return sorted_arr
# Example usage
numbers = [4, 2, 2, 8, 3, 3, 1]
sorted_numbers = counting_sort(numbers)
print("Sorted numbers using Counting Sort:", sorted_numbers)
#Radix Sort
#Radix Sort is a non-comparison-based sorting algorithm that sorts integers by processing individual digits
#from the least significant digit to the most significant digit. It uses a stable sorting algorithm, such as Counting Sort, as a subroutine to sort the digits. Here is an implementation of the Radix Sort algorithm in Python:    
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]  
def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr
# Example usage
numbers = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_numbers = radix_sort(numbers)    
print("Sorted numbers using Radix Sort:", sorted_numbers)

searching and sorting algorithms are fundamental concepts in computer science that are used to organize and retrieve data efficiently. Sorting algorithms arrange data in a specific order, while searching algorithms find specific elements within a dataset. Understanding these algorithms is crucial for optimizing performance and solving various computational problems.
