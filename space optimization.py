class Solution:
    def mark_multiple(self, a: int, b: int) -> str:
        bitmask = 0
        for i in range(b - a + 1):
            num = a + i
            if num % 2 == 0 or num % 5 == 0:
                bitmask |= (1 << i)
                print(f"Setting bit {i} for num {num}: bitmask = {bin(bitmask)[2:]}")

        result = []
        for i in range(b - a + 1):
            if (bitmask & (1 << i)) != 0:
                result.append(str(a + i))

        return " ".join(result)


if __name__ == "__main__":
    print("Result:", Solution().mark_multiple(2, 10))
