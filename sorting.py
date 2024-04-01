from random import randint
import time

def generate_array(size):
    """Generate an array of random integers."""
    arr = []
    for _ in range(size):
        arr.append(randint(0, 20000))
    return arr

def is_sorted(arr):
    """Check if the given array is sorted in ascending order."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def test_time():
    """Function for testing execution time of sorting algorithms."""
    # Display current time in seconds and CPU time
    print(time.time())
    print(time.perf_counter())

    # Generate an array of size 10000
    arr = generate_array(10000)

    # Measure the execution time of selection_sort_swap function
    start = time.perf_counter()
    out = selection_sort_swap(arr)
    end = time.perf_counter()

    # Display the execution time
    print(end - start)

def time_function(func, arr):
    """Measure the execution time of a sorting function."""
    # Make a copy of the input array
    arr_copy = arr[:]
    
    # Record the start time
    start = time.perf_counter()
    
    # Call the sorting function
    out = func(arr_copy)
    
    # Record the end time
    end = time.perf_counter()
    
    # Print the execution time along with sorting information
    print(f'{(end - start):.3f} seconds \t Sorted: {is_sorted(out)} \t {func.__name__}')
    
    # Return the execution time
    return end - start

def selection_sort(arr):
    """Sort the array using selection sort."""
    sorted_arr = []
    while arr:
        smallest = arr[0]
        smallest_index = 0
        for i, item in enumerate(arr):
            if smallest > item:
                smallest = item
                smallest_index = i
        sorted_arr.append(arr.pop(smallest_index))
        
    return sorted_arr

def selection_sort_swap(arr):
    """Sort the array using selection sort with swapping."""
    arr_len = len(arr)
    element = 0
    while element < arr_len:
        smallest = arr[element]
        smallest_index = element
        for i in range(element + 1, arr_len):
            if smallest > arr[i]:
                smallest = arr[i]
                smallest_index = i

        arr[element], arr[smallest_index] = arr[smallest_index], arr[element]
        element += 1
    return arr

def bubble_sort(arr):
    """Sort the array using bubble sort."""
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def weird_sort(arr):
    """Sort the array using a weird sort."""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
        
def insertion_sort(arr):
    """Sort the array using insertion sort."""
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr

def insertion_sort_faster(arr):
    """Sort the array using insertion sort with optimization."""
    for pivot in range(1, len(arr)):
        curr = arr[pivot]
        j = pivot - 1

        # Move elements in the sorted left array that are greater than curr
        # to one position ahead of their current position
        while j >= 0 and arr[j] > curr:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = curr  # Insert the key at its correct position

    return arr

def merge_sort(arr):
    """Sort the array using merge sort."""
    arr_size = len(arr)
    if arr_size <= 1:
        return arr

    left, right = arr[:arr_size // 2], arr[arr_size // 2:]

    left, right = merge_sort(left), merge_sort(right)

    output = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            output.append(left[left_index])
            left_index += 1
        else:
            output.append(right[right_index])
            right_index += 1

    output += left[left_index:]
    output += right[right_index:]
    
    return output   

def random_sort(arr):
    """Sort the array using a random sort."""
    from random import shuffle

    count = 0

    while not is_sorted(arr):
        count += 1
        shuffle(arr)

    return arr

def bucket_sort(arr, digit):
    """Sort the array using bucket sort."""
    # 10 buckets, one for each digit
    buckets = [[] for _ in range(10)]

    for val in arr:
        # Find the proper digit and put the value in that bucket
        curr_val = (val // digit) % 10
        buckets[curr_val].append(val)

    i = 0
    for bucket in buckets:
        for val in bucket:
            arr[i] = val
            i += 1
        

def radix_sort(arr):
    """Sort the array using radix sort."""
    # Get digits in max number
    max_val = max(arr)

    digit = 1
    while digit <= max_val:
        bucket_sort(arr, digit)
        digit *= 10

    return arr

# Generate array
arr = generate_array(100000)

# Test and time sorting algorithms
time_function(selection_sort, arr[:])
time_function(bubble_sort, arr[:])
time_function(weird_sort, arr[:])
time_function(insertion_sort, arr[:])
time_function(insertion_sort_faster, arr[:])
time_function(merge_sort, arr[:])
time_function(random_sort, arr[:3]) # Select only a subset of the array due to the randomness of this algorithm
time_function(radix_sort, arr[:])
