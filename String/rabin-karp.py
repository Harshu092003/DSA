def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    pattern_hash = sum(ord(c) for c in pattern)
    window_hash = sum(ord(text[i]) for i in range(m))
    print(window_hash)

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            # verify characters
            if text[i:i+m] == pattern:
                return i  # match found
        
        # update hash (rolling)
        if i < n - m:
            window_hash = window_hash - ord(text[i]) + ord(text[i + m])
    
    return -1

print(rabin_karp("helloabcworld", "abc"))  # Output: 5
