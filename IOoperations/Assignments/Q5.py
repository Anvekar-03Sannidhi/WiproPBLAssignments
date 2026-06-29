import os
import re

def longest_word_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    words = re.findall(r"\w+", text)
    if not words:
        return None
    return max(words, key=len)


def main():
    fname = input("Enter filename (or press Enter for sample.txt): ").strip() or 'sample.txt'
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        word = longest_word_in_file(path)
        if word is None:
            print("No words found in file.")
        else:
            print("Longest word:", word)
    except FileNotFoundError:
        print(f"File not found: {path}")


if __name__ == '__main__':
    main()
