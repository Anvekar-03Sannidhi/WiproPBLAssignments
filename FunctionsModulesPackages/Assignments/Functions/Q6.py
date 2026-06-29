def is_prime(n):
    """Return True if n is prime, False otherwise. Handles n<2 as non-prime."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    for x in range(0, 21):
        print(x, is_prime(x))
