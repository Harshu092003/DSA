def binary_exponentiation(x: int, n: int) -> int:
    result = 1
    base = x
    exponent = n
    step = 1

    print("Initial State")
    print(f"x = {x}, n = {n}, binary(n) = {bin(n)[2:]}")
    print("-" * 50)

    while exponent > 0:
        print(f"\nStep {step}")
        print(f"Exponent (decimal): {exponent}")
        print(f"Exponent (binary) : {bin(exponent)[2:]}")
        print(f"Current result    : {result}")
        print(f"Current base      : {base}")

        # Check last binary bit
        if exponent % 2 == 1:
            print("Last bit is 1 → result = result * base")
            result *= base
            print(f"Updated result    : {result}")
        else:
            print("Last bit is 0 → result unchanged")

        # Square the base
        base *= base
        print(f"Base squared      : {base}")

        # Shift exponent right
        exponent //= 2
        print(f"Exponent after //2: {exponent} (binary {bin(exponent)[2:] if exponent>0 else '0'})")

        step += 1
        print("-" * 50)

    print("\nFinal Result:", result)
    return result


# Example usage
x = 2
n = 10
binary_exponentiation(x, n)