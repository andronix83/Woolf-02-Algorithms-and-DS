# Food Energy Optimization Report: Greedy vs. Dynamic Programming

## 1. Project Overview
This project solves the "Knapsack Problem" using food items. The goal is to choose a set of food items that maximizes total calories without exceeding a budget of **100**.

We implemented and compared two algorithmic approaches:
1.  **Greedy Algorithm**
2.  **Dynamic Programming**

## 2. Algorithms Description

### Greedy Algorithm
* **Strategy:** This approach makes the locally optimal choice at each step. It calculates the "efficiency" of each item (Calories divided by Cost) and picks the most efficient items first.
* **Behavior:** It fills the basket with high-value items immediately, hoping this leads to the best overall result.

### Dynamic Programming
* **Strategy:** This approach breaks the problem down into smaller sub-problems. It builds a table to calculate the maximum calories possible for every budget amount up to the limit.
* **Behavior:** It considers all possible combinations to find the mathematical maximum.

## 3. Results Comparison

Based on the program execution with a budget of **100**:

| Algorithm | Selected Items | Total Cost | Total Calories |
| :--- | :--- | :--- | :--- |
| **Greedy** | `cola`, `potato`, `pepsi`, `hot-dog` | 80 | **870** |
| **Dynamic Programming** | `potato`, `cola`, `pepsi`, `pizza` | 100 | **970** |

## 4. Analysis

### Why did the results differ?
The **Greedy Algorithm** selected items with the best calorie-to-cost ratio first (e.g., Cola and Potato). However, after picking the "Hot-dog" (Cost: 30), it hit a total cost of 80. It had **20** budget units left, but no item costs 20 or less. Therefore, that budget space was wasted, resulting in fewer total calories (870).

**Dynamic Programming** looked at the "big picture." It realized that by skipping the "Hot-dog" and choosing the "Pizza" (Cost: 50) instead, it could use exactly 100% of the budget. This perfect fit allowed it to achieve a higher total calorie count (970).

## 5. Conclusion

* **Greedy Algorithm:** Is very fast and simple to code. However, it provides an **approximation**, not always the best solution. It failed to utilize the full budget in this specific case.
* **Dynamic Programming:** Guarantees the **optimal solution** (the absolute best result). It successfully found a combination that maximized calories by using the entire budget efficiently.

**Final Verdict:** For this specific dataset and budget, **Dynamic Programming is the superior approach**, yielding **100 more calories** than the Greedy approach.