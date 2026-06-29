import os

def read_first_n(filepath, n):
    lines = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for _ in range(n):
            line = f.readline()
            if not line:
                break
            lines.append(line.rstrip('\n'))
    return lines


def main():
    fname = input("Enter filename (or press Enter for sample.txt): ").strip() or 'sample.txt'
    try:
        n = int(input("Enter number of lines to read (n): ").strip())
    except ValueError:
        print("Invalid number")
        return
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        lines = read_first_n(path, n)
        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"File not found: {path}")


if __name__ == '__main__':
    main()
