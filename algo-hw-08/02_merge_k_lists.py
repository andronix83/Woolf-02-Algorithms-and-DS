import heapq


def merge_k_lists(lists):
    """
    Merges k sorted lists into one sorted list using a Min-Heap.
    """
    min_heap = []

    # 1. Initialization: add the first element from each list to the heap.
    # list_index is needed to know which list to fetch the next element from.
    for i, lst in enumerate(lists):
        if lst:  # Check if the list is not empty
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged_list = []

    # 2. Main loop: while there are elements in the heap
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)

        # Append the smallest element to the result
        merged_list.append(val)

        # 3. Add the next element from the same list if it exists
        next_element_idx = element_idx + 1
        if next_element_idx < len(lists[list_idx]):
            next_val = lists[list_idx][next_element_idx]
            heapq.heappush(min_heap, (next_val, list_idx, next_element_idx))

    return merged_list


def main() -> None:
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Sorted list (Heap):", merged_list)


if __name__ == "__main__":
    main()