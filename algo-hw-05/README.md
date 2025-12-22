# Substring Search Algorithms: Performance Analysis

## Overview
This project compares the efficiency of three popular substring search algorithms:
1.  **Boyer-Moore** (with Bad Character Heuristic)
2.  **Knuth-Morris-Pratt (KMP)**
3.  **Rabin-Karp**

The goal was to determine which algorithm performs best on large text files containing mixed English and Ukrainian content.

## Test Environment
The benchmark was conducted on the following hardware and software configuration:
* **CPU:** Intel Core i7-1185G7
* **RAM:** 32 GB
* **OS:** Windows 11
* **Language:** Python 3.13

## Benchmark Results

The tests measured the execution time (average of 100 runs) for finding two types of patterns:
1.  **Existing:** A word that actually exists in the text.
2.  **Non-Existing:** A phrase that does not exist (forcing the algorithm to scan the entire file).

### File 1: `text-1-ukr.txt`
| Algorithm | Pattern Type | Time (sec) |
| :--- | :--- | :--- |
| **Boyer-Moore** | Existing ('послідовність') | **0.00568** |
| KMP | Existing | 0.03100 |
| Rabin-Karp | Existing | 0.05313 |
| **Boyer-Moore** | Non-Existing ('сферичний кінь') | **0.07003** |
| KMP | Non-Existing | 0.49193 |
| Rabin-Karp | Non-Existing | 0.51547 |

### File 2: `text-2-ukr.txt`
| Algorithm | Pattern Type | Time (sec) |
| :--- | :--- | :--- |
| **Boyer-Moore** | Existing ('розгорнутий список') | **0.00478** |
| KMP | Existing | 0.03451 |
| Rabin-Karp | Existing | 0.04085 |
| **Boyer-Moore** | Non-Existing ('адронний колайдер') | **0.06809** |
| KMP | Non-Existing | 0.61586 |
| Rabin-Karp | Non-Existing | 0.85890 |

## Performance Analysis

### 1. Boyer-Moore (The Winner)
Boyer-Moore was the **fastest algorithm** in every test case.
* **Why:** It uses the "Bad Character Heuristic" to skip sections of the text. Instead of checking every character, it jumps ahead when a mismatch occurs.
* **Impact:** For non-existing patterns (scanning the whole file), it was approximately **7-9 times faster** than KMP and Rabin-Karp.

### 2. Knuth-Morris-Pratt (KMP)
KMP took second place.
* **Why:** It is a stable, linear algorithm $O(N)$. It avoids re-checking characters it has already matched, but it still visits many more characters than Boyer-Moore.
* **Observation:** It is reliable, but in Python, the overhead of the loop logic makes it slower than the "skipping" strategy of Boyer-Moore.

### 3. Rabin-Karp (The Slowest)
Rabin-Karp was the slowest algorithm in this benchmark.
* **Why:** This algorithm relies on calculating rolling hashes. In Python, performing mathematical operations (multiplication and modulus) for every window of text is computationally expensive compared to simple character comparisons.

## Conclusion
For searching text files with natural language (English/Ukrainian) in Python, the **Boyer-Moore** algorithm is significantly more efficient than KMP or Rabin-Karp. It is the recommended choice for this specific use case.