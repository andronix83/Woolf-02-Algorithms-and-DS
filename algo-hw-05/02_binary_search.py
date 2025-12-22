def binary_search_upper_bound(sorted_array, target):
    low = 0
    high = len(sorted_array) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        # Increment iteration count
        iterations += 1

        mid = (low + high) // 2

        if sorted_array[mid] < target:
            # If the middle element is less than target, ignore left half
            low = mid + 1
        else:
            # If element is >= target, it's a candidate for upper bound
            upper_bound = sorted_array[mid]
            # Try to find a smaller valid element in the left half
            high = mid - 1

    return iterations, upper_bound


def main():
    # Example usage with floating point numbers
    data = [1.1, 1.3, 2.5, 3.8, 4.2, 5.5, 6.7, 8.1, 9.4]
    target_value = 4.0

    result = binary_search_upper_bound(data, target_value)

    print(f"Array: {data}")
    print(f"Target: {target_value}")
    print(f"Result (Iterations, Upper Bound): {result}")


if __name__ == "__main__":
    main()