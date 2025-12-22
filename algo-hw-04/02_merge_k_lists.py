def merge_two_lists(list1, list2):
    """
    Helper function to merge two sorted lists into one sorted list.
    """
    merged = []
    i, j = 0, 0

    # Traverse both lists and append the smaller element to the merged list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any remaining elements from list1
    if i < len(list1):
        merged.extend(list1[i:])

    # Append any remaining elements from list2
    if j < len(list2):
        merged.extend(list2[j:])

    return merged

def merge_k_lists(lists):
    """
    Merges k sorted lists using the Divide and Conquer approach.
    Time Complexity: O(N log k) where N is total elements and k is number of lists.
    """
    # Base case: if the input list of lists is empty
    if not lists:
        return []

    # Base case: if there is only one list, return it
    if len(lists) == 1:
        return lists[0]

    # Divide step: find the middle index
    mid = len(lists) // 2

    # Recursive calls: divide the lists into two halves
    left_merged = merge_k_lists(lists[:mid])
    right_merged = merge_k_lists(lists[mid:])

    # Conquer step: merge the two sorted results
    return merge_two_lists(left_merged, right_merged)

def main() -> None:
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    result = merge_k_lists(lists)
    print("Sorted list: ", result)


if __name__ =="__main__":
    main()