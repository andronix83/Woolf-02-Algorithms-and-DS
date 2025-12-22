import timeit
import os


# ==========================================
# Algorithm Implementations
# ==========================================

def kmp_search(pattern, text):
    """
    Knuth-Morris-Pratt (KMP) search algorithm.
    """
    m = len(pattern)
    n = len(text)

    # Create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * m
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    compute_lps_array(pattern, m, lps)

    i = 0  # index for text[]
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            # Pattern found at index i - j
            return i - j
            # j = lps[j-1] # Continue searching if needed
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def compute_lps_array(pattern, m, lps):
    """
    Helper function for KMP to compute Longest Prefix Suffix array.
    """
    length = 0
    lps[0] = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def bm_search(pattern, text):
    """
    Boyer-Moore search algorithm using Bad Character Heuristic.
    """
    m = len(pattern)
    n = len(text)

    # Use a dictionary to handle Unicode characters
    bad_char = {}

    # Fill the bad character table
    for i in range(m):
        bad_char[ord(pattern[i])] = i

    s = 0
    while s <= n - m:
        j = m - 1

        # Keep reducing j while characters of pattern and text are matching
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            # Pattern found at index s
            return s
        else:
            # Shift the pattern so that the bad character in text
            # aligns with the last occurrence of it in pattern.
            s += max(1, j - bad_char.get(ord(text[s + j]), -1))

    return -1


def rk_search(pattern, text):
    """
    Rabin-Karp search algorithm using rolling hash.
    """
    d = 256  # Number of characters in the input alphabet
    q = 101  # A prime number
    m = len(pattern)
    n = len(text)
    i = 0
    j = 0
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text
    h = 1

    # The value of h would be "pow(d, m-1)%q"
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        if p == t:
            # Check for characters one by one
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == m:
                return i  # Pattern found

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


# ==========================================
# Benchmarking & Analysis Logic
# ==========================================

def run_benchmark(filename, pattern_existing, pattern_non_existing):
    """
    Runs timeit for all algorithms on a specific file.
    """
    print(f"\n--- Analyzing file: {filename} ---")

    if not os.path.exists(filename):
        print(f"Error: File {filename} not found.")
        return None

    with open(filename, 'r', encoding='utf-8') as f:
        text_content = f.read()

    algorithms = [
        ("Boyer-Moore", bm_search),
        ("Knuth-Morris-Pratt", kmp_search),
        ("Rabin-Karp", rk_search)
    ]

    results = {}

    patterns = [
        ("Existing", pattern_existing),
        ("Non-Existing", pattern_non_existing)
    ]

    for p_type, pattern in patterns:
        print(f"  Testing {p_type} pattern: '{pattern}'")
        for name, func in algorithms:
            # Set up the timer
            timer = timeit.Timer(lambda: func(pattern, text_content))
            # Run 100 times to get average execution time
            try:
                exec_time = timer.timeit(number=100)
                results[(name, p_type)] = exec_time
                print(f"    {name}: {exec_time:.5f} sec")
            except Exception as e:
                print(f"    {name}: Error ({e})")
                results[(name, p_type)] = float('inf')

    # Find the winner for this file (total time)
    best_algo = min(algorithms, key=lambda x: results.get((x[0], "Existing"), 0)
                                              + results.get((x[0], "Non-Existing"), 0))

    print(f"  >> Fastest algorithm for {filename}: {best_algo[0]}")

    return results


def main():
    # Define file paths
    files_subfolder = "text_samples"
    text1 = os.path.join(files_subfolder, "text-1-ukr.txt")
    text2 = os.path.join(files_subfolder, "text-2-ukr.txt")

    # Define patterns to search
    p1_exist = "послідовність"
    p1_fake = "сферичний кінь"

    p2_exist = "розгорнутий список"
    p2_fake = "адронний колайдер"

    # Run benchmarks
    result1 = run_benchmark(text1, p1_exist, p1_fake)
    result2 = run_benchmark(text2, p2_exist, p2_fake)

    # Global analysis
    if result1 and result2:
        print("\n=== Global Analysis ===")

        total_times = {
            "Boyer-Moore": 0,
            "Knuth-Morris-Pratt": 0,
            "Rabin-Karp": 0
        }

        for key, time_val in result1.items():
            algo_name = key[0]
            total_times[algo_name] += time_val

        for key, time_val in result2.items():
            algo_name = key[0]
            total_times[algo_name] += time_val

        overall_winner = min(total_times, key=total_times.get)

        print("Total execution time (all tests):")
        for algo, t in total_times.items():
            print(f"  {algo}: {t:.5f} sec")

        print(f"\nOVERALL CHAMPION: {overall_winner}")


if __name__ == "__main__":
    main()