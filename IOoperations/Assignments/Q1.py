import os

def read_all(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    fname = input("Enter filename (or press Enter for sample.txt): ").strip() or 'sample.txt'
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        content = read_all(path)
        print(content)
    except FileNotFoundError:
        print(f"File not found: {path}")


if __name__ == '__main__':
    main()
