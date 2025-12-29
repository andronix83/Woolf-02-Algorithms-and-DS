def greedy_algorithm(items, budget):
    """
    Greedy algorithm to select food items based on calorie-to-cost ratio.
    """
    # Create a list of items with their efficiency (calories per cost unit)
    item_list = []
    for name, details in items.items():
        cost = details["cost"]
        calories = details["calories"]
        # Avoid division by zero if cost is 0 (though unlikely in this context)
        ratio = calories / cost if cost > 0 else 0
        item_list.append({
            "name": name,
            "cost": cost,
            "calories": calories,
            "ratio": ratio
        })

    # Sort items by ratio in descending order (highest efficiency first)
    item_list.sort(key=lambda x: x["ratio"], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    for item in item_list:
        if total_cost + item["cost"] <= budget:
            chosen_items.append(item["name"])
            total_cost += item["cost"]
            total_calories += item["calories"]

    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    """
    Dynamic programming algorithm to find the optimal set of food items
    maximizing calories within the budget (0/1 Knapsack Problem).
    """
    # Extract data into lists for easier indexing
    names = list(items.keys())
    costs = [items[n]["cost"] for n in names]
    calories = [items[n]["calories"] for n in names]
    n = len(items)

    # Initialize DP table: rows = items (0 to n), cols = budget (0 to budget)
    # K[i][w] will store the max calories using first i items with budget w
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            item_cost = costs[i - 1]
            item_calories = calories[i - 1]

            if item_cost <= w:
                # Max of: including the item OR excluding the item
                K[i][w] = max(
                    item_calories + K[i - 1][w - item_cost],
                    K[i - 1][w]
                )
            else:
                # If item cost is more than current budget limit w, exclude it
                K[i][w] = K[i - 1][w]

    # Traceback to find which items were selected
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        # If the value comes from the row above, the item was NOT included.
        # If it's different, the item WAS included.
        if K[i][w] != K[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]

    # The result in the table is the max calories
    max_calories = K[n][budget]

    # Calculate total cost for verification
    total_cost = sum(items[item]["cost"] for item in selected_items)

    return selected_items, max_calories, total_cost


# --- Testing the algorithms ---
def main() -> None:
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget_limit = 100

    print(f"Budget: {budget_limit}\n")

    # 1. Greedy Algorithm Execution
    greedy_items, greedy_cals, greedy_cost = greedy_algorithm(items, budget_limit)
    print("--- Greedy Algorithm ---")
    print(f"Selected items: {greedy_items}")
    print(f"Total Cost: {greedy_cost}")
    print(f"Total Calories: {greedy_cals}")

    print("\n")

    # 2. Dynamic Programming Execution
    dp_items, dp_cals, dp_cost = dynamic_programming(items, budget_limit)
    print("--- Dynamic Programming ---")
    print(f"Selected items: {dp_items}")
    print(f"Total Cost: {dp_cost}")
    print(f"Total Calories: {dp_cals}")


if __name__ == "__main__":
    main()