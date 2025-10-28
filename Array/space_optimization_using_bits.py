def mark_multiples(a, b):
    bitmask = 0  # Initialize bitmask with all bits 0

    # Mark multiples of 2 or 5
    for i in range(b - a + 1):
        num = a + i
        if num % 2 == 0 or num % 5 == 0:
            bitmask |= 1 << i  # Set bit i

    # Print all marked multiples
    result = []
    for i in range(b - a + 1):
        if (bitmask & (1 << i)) != 0:
            result.append(str(a + i))

    print(" ".join(result))


# Example usage:
if __name__ == "__main__":
    mark_multiples(2, 10)  # Output: 2 4 5 6 8 10
    mark_multiples(
        60, 95
    )  # Output: 60 62 64 65 66 68 70 72 74 75 76 78 80 82 84 85 86 88 90 92 94 95
