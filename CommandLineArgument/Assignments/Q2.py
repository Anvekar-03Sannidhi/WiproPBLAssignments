import sys
import os


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("Usage: python Q2.py <welcome message...>")
        return 1
    message = ' '.join(argv)
    filename = os.path.basename(__file__)
    print(f"{message} - {filename}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
