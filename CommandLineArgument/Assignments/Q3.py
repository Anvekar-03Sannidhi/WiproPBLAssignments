import sys


def is_prime(n: int) -> bool:
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


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 10:
        print("Usage: python Q3.py n1 n2 ... n10")
        return 1
    try:
        nums = [int(x) for x in argv[:10]]
    except ValueError:
        print("All arguments must be integers.")
        return 1
    s = sum(x for x in nums if is_prime(x))
    print(s)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
