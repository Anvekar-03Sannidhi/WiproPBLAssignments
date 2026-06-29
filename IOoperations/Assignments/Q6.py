import os
import re

def count_word_in_file(filepath, word):
    pattern = re.compile(r"\b" + re.escape(word) + r"\b", flags=re.IGNORECASE)
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    return len(pattern.findall(text))


def main():
    fname = input("Enter filename (or press Enter for sample.txt): ").strip() or 'sample.txt'
    word = input("Enter the word to count: ").strip()
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        cnt = count_word_in_file(path, word)
        print(f"'{word}' appears {cnt} time(s) in {fname}")
    except FileNotFoundError:
        print(f"File not found: {path}")


if __name__ == '__main__':
    main()
