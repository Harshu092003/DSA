def getBit(num, i):
    return (num & (1 << i)) != 0


def setBit(num, i):
    return num | (1 << i)


def clearBit(num, i):
    return num & ~(1 << i)


if __name__ == "__main__":
    number = 43  # binary: 00101011

    print(f"Number = {number} (binary: {bin(number)})\n")

    print("Get Bit Results:")
    for bit_pos in range(8):
        bit_val = getBit(number, bit_pos)
        print(f"  Bit position {bit_pos}: {1 if bit_val else 0}")

    print("\nSet Bit Results (setting bit at each position):")
    for bit_pos in range(8):
        new_num = setBit(number, bit_pos)
        print(f"  Set bit {bit_pos}: {new_num} (bin: {bin(new_num)})")

    print("\nClear Bit Results (clearing bit at each position):")
    for bit_pos in range(8):
        new_num = clearBit(number, bit_pos)
        print(f"  Clear bit {bit_pos}: {new_num} (bin: {bin(new_num)})")


# Example: if X=1010₂ (binary 10)
# X ⊕ 0s = 1010₂ (unchanged)
# X ⊕ 1s = 0101₂ (bitwise complement)
# X & 0s = 0000₂ (cleared bits)
# X & 1s = 1010₂ (unchanged)
# X | 0s = 1010₂ (unchanged)
# X | 1s = 1111₂ (all bits set)
