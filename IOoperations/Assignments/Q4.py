import os

def read_lines_into_list(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


def main():
    fname = input("Enter filename (or press Enter for sample.txt): ").strip() or 'sample.txt'
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        lines = read_lines_into_list(path)
        print(lines)
    except FileNotFoundError:
        print(f"File not found: {path}")


if __name__ == '__main__':
    main()
