import random
import timeit
import sys

# Increase recursion depth limit for large mergesort
sys.setrecursionlimit(2000)


def insertion_sort(arr):
    """
    Implementation of Insertion Sort algorithm.
    Time Complexity: O(n^2)
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    """
    Implementation of Merge Sort algorithm.
    Time Complexity: O(n log n)
    """
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sorting the first half
        merge_sort(left_half)

        # Sorting the second half
        merge_sort(right_half)

        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def run_benchmark():
    """
    Generates data and runs timeit comparisons for different array sizes.
    """
    # Define test sizes: Small, Medium, Large
    sizes = [100, 1000, 10000]

    print(f"{'Algorithm':<20} | {'Array Size':<10} | {'Time (seconds)':<15}")
    print("-" * 55)

    for size in sizes:
        # Generate random data for this size
        original_data = [random.randint(0, 100000) for _ in range(size)]

        # --- Test 1: Insertion Sort ---
        # We perform a copy of data inside the lambda to ensure fair testing on unsorted data
        test_data = original_data[:]
        time_insertion = timeit.timeit(lambda: insertion_sort(test_data.copy()), number=1)
        print(f"{'Insertion Sort':<20} | {size:<10} | {time_insertion:.6f}")

        # --- Test 2: Merge Sort ---
        test_data = original_data[:]
        time_merge = timeit.timeit(lambda: merge_sort(test_data.copy()), number=1)
        print(f"{'Merge Sort':<20} | {size:<10} | {time_merge:.6f}")

        # --- Test 3: Python Built-in Sort (Timsort) ---
        test_data = original_data[:]
        time_builtin = timeit.timeit(lambda: test_data.copy().sort(), number=1)
        print(f"{'Built-in (Timsort)':<20} | {size:<10} | {time_builtin:.6f}")

        print("-" * 55)


if __name__ == "__main__":
    print("Starting Benchmark...\n")
    run_benchmark()
    print("\nBenchmark finished.")