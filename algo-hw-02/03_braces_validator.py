from collections import deque


def validate_braces(s: str) -> bool:
    """
    Validates if the braces () {} [] in a string are balanced and correctly
    nested using a collections.deque for the stack implementation.
    """

    # Use a deque as a stack for efficient O(1) push and pop operations
    stack = deque()

    # Define mapping of closing to opening braces
    brace_map = {")": "(", "}": "{", "]": "["}

    opening_braces = set(brace_map.values())
    closing_braces = set(brace_map.keys())

    # Iterate through each character in the string
    for char in s:
        if char in opening_braces:
            # If it's an opening brace, push it onto the stack.
            stack.append(char)
        elif char in closing_braces:
            # If it's a closing brace:

            # 1. Check if the stack is empty.
            if not stack:
                return False

            # 2. Pop the top element from the stack.
            top_element = stack.pop()

            # 3. Check for a match.
            if brace_map[char] != top_element:
                return False

    # The braces are balanced if the stack is completely empty at the end.
    return len(stack) == 0

def main() -> None:
    test_strings = [
        "()",          # Valid
        "([])",        # Valid
        "{[()]}",      # Valid
        "({[]})",      # Valid
        "((()))",      # Valid
        "([{}])",      # Valid

        "(",           # Invalid
        ")",           # Invalid
        "([)]",        # Invalid
        "{[(])}",      # Invalid
        "((())",       # Invalid
        "())",         # Invalid

        "abc(def)[ghi]{jkl}",  # Valid with other characters
        "abc(def[ghi]{jkl}",   # Invalid with other characters
    ]

    print("Brace Validation Results:")
    for s in test_strings:
        result = validate_braces(s)
        checkmark = "✅" if result else "❌"
        print(f"{checkmark} {s}")


if __name__ =="__main__":
    main()