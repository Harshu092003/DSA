def pairInSortedRotated(arr, target):
    s = set()
    for num in arr:
        complement = target - num
        if complement in s:
            return True, (complement, num)  # Return True and the pair
        s.add(num)

    return False, None  # No pair found

if __name__ == "__main__":
    arr = [11, 15, 6, 8, 9, 10]
    target = 16

    found, pair = pairInSortedRotated(arr, target)
    if found:
        print("true")
        print("Pair found:", pair)
    else:
        print("false")
