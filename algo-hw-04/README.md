# Sorting Algorithms Benchmark

This project compares the performance of three sorting approaches in Python:
1. **Insertion Sort** (Custom implementation)
2. **Merge Sort** (Custom implementation)
3. **Built-in Sort** (Python's standard `list.sort()` / Timsort)

## Environment
The benchmark was executed on the following hardware:
* **CPU:** Intel Core i7-1185G7
* **RAM:** 32GB
* **Language:** Python 3.13
* **Operating System:** Windows 11

## Benchmark Results

| Algorithm | Array Size | Time (seconds) |
| :--- | :--- | :--- |
| **Insertion Sort** | 100 | 0.000121 |
| **Merge Sort** | 100 | 0.000087 |
| **Built-in (Timsort)** | 100 | 0.000006 |
| | | |
| **Insertion Sort** | 1,000 | 0.014435 |
| **Merge Sort** | 1,000 | 0.001094 |
| **Built-in (Timsort)** | 1,000 | 0.000073 |
| | | |
| **Insertion Sort** | 10,000 | 1.605051 |
| **Merge Sort** | 10,000 | 0.018656 |
| **Built-in (Timsort)** | 10,000 | 0.001008 |

## Performance Analysis

### 1. Insertion Sort (The Slowest)
* **Behavior:** It performs decently on very small arrays (100 items). However, as the data grows, the execution time increases drastically.
* **Reason:** It has a time complexity of **O(n²)**. Increasing the input from 1,000 to 10,000 (10x increase) caused the time to jump from ~0.01s to ~1.60s (roughly a 100x increase).
* **Verdict:** Inefficient for large datasets.

### 2. Merge Sort (Balanced)
* **Behavior:** It scales much better than Insertion Sort. Even with 10,000 items, it finished in roughly 0.018 seconds.
* **Reason:** It has a time complexity of **O(n log n)**. It handles larger datasets efficiently by dividing the problem into smaller sub-problems.
* **Verdict:** Good for algorithmic understanding, but slower than the built-in method due to Python's interpreter overhead.

### 3. Built-in Timsort (The Winner)
* **Behavior:** It is orders of magnitude faster than the custom implementations. Even at 10,000 items, it is nearly instant (0.001s).
* **Reason:**
    1.  **C Implementation:** Python's built-in functions are written in C, which is much faster than interpreted Python code.
    2.  **Optimization:** Timsort is a hybrid algorithm (derived from Merge Sort and Insertion Sort) designed to take advantage of existing order in real-world data.
* **Verdict:** Always use the standard `list.sort()` or `sorted()` in production code.

## Conclusion
The benchmark proves that Python's **built-in sorting algorithm is superior**. For an array of 10,000 elements, the built-in sort is approximately **18 times faster than Merge Sort** and **1,600 times faster than Insertion Sort**.