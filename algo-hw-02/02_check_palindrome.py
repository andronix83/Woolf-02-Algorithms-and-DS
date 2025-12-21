from collections import deque


def check_palindrome(text) -> bool:
    """
    Checks if a string is a palindrome using collections.deque.
    Ignores case, whitespace, and punctuation marks.
    """
    # 1. Pre-processing: Create a list of valid characters
    cleaned_chars = [char.lower() for char in text if char.isalnum()]

    # 2. Create a double-ended queue from the cleaned characters
    char_deque = deque(cleaned_chars)

    # 3. Compare characters from both ends
    while len(char_deque) > 1:
        first = char_deque.popleft()  # Remove and return the first element
        last = char_deque.pop()  # Remove and return the last element
        if first != last:
            return False  # Mismatch found, not a palindrome

    # If the loop finishes without mismatches - it is a palindrome
    return True

def main() -> None:
    popular_palindromes = [
        # English palindromes
        "Madam, I'm Adam",
        "A man, a plan, a canal: Panama",
        "A Toyota's a Toyota",
        "Eva, can I see bees in a cave?",
        "Do geese see God?",
        "Was it a car or a cat I saw?",
        "Never odd or even",

        # Ukrainian palindromes
        "Я несу гусеня",
        "Козак з казок",
        "Кит на морі романтик",
        "Три психи пили Пилипихи спирт",
        "Де помити мопед?",

        # Russian palindromes
        "А роза упала на лапу Азора",
        "Аргентина манит негра",
        "Леша на полке клопа нашел",
        "Около Миши молоко",

        # Non-palindromes (just for testing)
        "Hello World",
        "Algorithms and Data Structures",
        "Це просто речення"
    ]

    print("\nChecking popular palindromes:")
    for palindrome in popular_palindromes:
        result = check_palindrome(palindrome)
        checkmark = "✅" if result else "❌"
        print(f'{checkmark} {palindrome}')

if __name__ == '__main__':
    main()