import os

def append_text(filepath, text):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(text + '\n')


def main():
    fname = input("Enter filename to append to (or press Enter for sample.txt): ").strip() or 'sample.txt'
    text = input("Enter text to append: ")
    path = os.path.join(os.path.dirname(__file__), fname)
    append_text(path, text)
    print(f"Appended to {path}")


if __name__ == '__main__':
    main()
