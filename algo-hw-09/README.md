# Coin Change Algorithms: Greedy vs. Dynamic Programming

This project implements and compares two algorithms for the "Change Making Problem." The goal is to determine the optimal number of coins needed to return a specific amount of change.

## 1. Algorithms Implemented

### Greedy Algorithm (`find_coins_greedy`)
* **How it works:** It always picks the largest available coin denomination first.
* **Pros:** Extremely fast and efficient.
* **Cons:** Does not guarantee the minimum number of coins for *all* possible coin systems (though it works for standard currency systems like USD or UAH).

### Dynamic Programming (`find_min_coins`)
* **How it works:** It builds a solution from the bottom up, calculating the minimum coins needed for every amount from 0 up to the target `amount`.
* **Pros:** Guaranteed to find the absolute minimum number of coins for **any** set of denominations.
* **Cons:** Much slower and requires more memory, especially for large amounts.

---

## 2. Performance Analysis

We compared the execution time of both algorithms on various amounts to analyze their efficiency.

### Test Environment
* **CPU:** Intel Core i7-1185G7
* **RAM:** 32GB
* **OS:** Windows 11
* **Python:** 3.13

### Benchmark Results

| Amount | Greedy Time (sec) | DP Time (sec) | Difference (DP/Greedy) |
| :--- | :--- | :--- | :--- |
| **100** | 0.000005 | 0.000297 | **56.0x slower** |
| **1,000** | 0.000004 | 0.003348 | **929.9x slower** |
| **2,000** | 0.000004 | 0.007226 | **2,064.3x slower** |
| **5,000** | 0.000005 | 0.020726 | **4,505.6x slower** |
| **10,000** | 0.000005 | 0.039808 | **7,371.6x slower** |
| **20,000** | 0.000006 | 0.077160 | **12,860.2x slower** |

### Key Findings

1.  **Greedy is Constant Time $O(1)$:**
    As seen in the table, the time for the Greedy algorithm stays almost exactly the same (~0.000005 seconds), regardless of whether the amount is 100 or 20,000. This is because it uses simple mathematical division and depends only on the number of coin types (6), not the total amount.

2.  **Dynamic Programming is Linear Time $O(N)$:**
    The DP algorithm's time grows directly in proportion to the `amount`.
    * When the amount increases from **2,000** to **20,000** (10x increase), the time increases from **0.007s** to **0.077s** (roughly 10x increase).
    * This confirms the complexity is $O(A \cdot K)$, where $A$ is the amount and $K$ is the number of coins.

3.  **Efficiency Gap:**
    For small sums, the difference is negligible to the human eye. However, as the amount grows, the gap becomes massive. At 20,000 units, the **DP algorithm is almost 13,000 times slower** than the Greedy approach.

## 3. Conclusion

* **Use the Greedy Algorithm** for real-world cash systems (like US Dollars, Euros, Hryvnias). It provides the correct answer instantly, even for massive amounts.
* **Use Dynamic Programming** only when dealing with non-standard arbitrary coin systems (e.g., if you had coins like 1, 3, and 4) where a greedy approach might fail to find the optimal solution.
