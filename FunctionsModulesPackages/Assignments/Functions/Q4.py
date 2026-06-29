def count_case(s):
    """Return tuple (upper_count, lower_count) for string s."""
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower


if __name__ == "__main__":
    sample = "Hello World! PYthon 3"
    u, l = count_case(sample)
    print(f"Uppercase: {u}, Lowercase: {l}")
