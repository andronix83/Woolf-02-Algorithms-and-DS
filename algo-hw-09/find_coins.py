import timeit


def find_coins_greedy(amount) -> dict[int, int]:
    """
    Calculates the change using a greedy algorithm.
    Time Complexity: O(K), where K is the number of coin denominations.
    It depends only on the number of coin types, not the amount size.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount = amount % coin

    return result


def find_min_coins(amount) -> dict[int, int]:
    """
    Calculates the minimum number of coins using dynamic programming.
    Time Complexity: O(A * K), where A is the amount and K is the number of coin denominations.
    Space Complexity: O(A) to store the DP table.
    """
    coins = [50, 25, 10, 5, 2, 1]

    # Initialize DP array: min_coins[i] stores the minimum coins needed for amount i
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    # To reconstruct the path (which coins were used), we track the last coin added
    last_coin_used = [0] * (amount + 1)

    for s in range(1, amount + 1):
        for coin in coins:
            if s >= coin:
                if min_coins[s - coin] + 1 < min_coins[s]:
                    min_coins[s] = min_coins[s - coin] + 1
                    last_coin_used[s] = coin

    # Reconstruct the result dictionary
    result = {}
    current_sum = amount

    while current_sum > 0:
        coin = last_coin_used[current_sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_sum -= coin

    return result


def compare_efficiency() -> None:
    """
    Runs performance tests on both algorithms using timeit.
    Tests various amounts to demonstrate Big O behavior.
    """
    # Test amounts: small, medium, and large to show scaling
    test_amounts = [100, 1000, 2000, 5000, 10000, 20000]

    print(f"{'Amount':<10} | {'Greedy Time (sec)':<20} | {'DP Time (sec)':<20} | {'Difference (DP/Greedy)':<25}")
    print("-" * 85)

    for amount in test_amounts:
        # Use lambda to pass arguments to the functions
        # number=10: We run it 10 times and take the total time to average out fluctuations
        # For very large DP arrays, many iterations would be too slow
        iterations = 10

        greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=iterations)
        dp_time = timeit.timeit(lambda: find_min_coins(amount), number=iterations)

        # Calculate how many times slower DP is compared to Greedy
        # Adding a small epsilon to avoid division by zero if greedy is too fast
        ratio = dp_time / (greedy_time + 1e-10)

        print(f"{amount:<10} | {greedy_time:.6f}{'':<12} | {dp_time:.6f}{'':<12} | {ratio:.1f}x slower")


if __name__ == "__main__":
    compare_efficiency()