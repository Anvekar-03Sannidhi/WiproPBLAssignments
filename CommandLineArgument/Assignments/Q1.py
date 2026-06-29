import sys


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 2:
        print("Usage: python Q1.py <num1> <num2>")
        return 1
    try:
        a = float(argv[0])
        b = float(argv[1])
    except ValueError:
        print("Both arguments must be numbers.")
        return 1
    print(a + b)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
