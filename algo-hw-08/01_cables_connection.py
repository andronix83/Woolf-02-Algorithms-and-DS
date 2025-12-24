import heapq


def min_cost_to_connect_cables(cables) -> int:
    """
    Calculates the minimum cost to connect cables and logs each step.
    """
    if not cables:
        print("No cables to connect.")
        return 0

    if len(cables) == 1:
        print(f"Only one cable provided: {cables[0]}. No connection needed.")
        return 0

    # Create a copy to avoid modifying the original list
    heap = list(cables)
    heapq.heapify(heap)

    total_cost = 0
    step = 1

    print(f"Initial heap: {heap}\n")

    while len(heap) > 1:
        # Extract two smallest cables
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)

        # Calculate cost for this specific connection
        current_cost = cable1 + cable2
        total_cost += current_cost

        print(f"-------- Step {step} --------")
        print(f"Connected cables: {cable1} + {cable2}")
        print(f"Cost of this connection: {current_cost}")
        print(f"Running total cost: {total_cost}")

        # Push the combined cable back to heap
        heapq.heappush(heap, current_cost)
        print(f"Heap state after push: {heap}\n")

        step += 1

    return total_cost


def main() -> None:
    cable_lengths = [4, 3, 5, 2, 6]

    print(f"Input: {cable_lengths}")

    result = min_cost_to_connect_cables(cable_lengths)

    print(f"Final Minimum Cost: {result}")


if __name__ == "__main__":
    main()