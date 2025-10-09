def binary_exponentiation(x: int, n: int) -> int:
    result = 1
    base = x
    exponent = n

    while exponent > 0:
        # If the current exponent bit is 1, multiply result by base
        if exponent % 2 == 1:
            result *= base
        # Square the base
        base *= base
        # Shift exponent right by 1 bit (divide by 2)
        exponent //= 2

    return result

# Example usage:
x = 2
n = 10
print(binary_exponentiation(x, n))  # Output: 1024

