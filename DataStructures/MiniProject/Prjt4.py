def count_name_occurrences(text, name="Alex"):
    
    return text.count(name)

def main():
    sample = "Hi Alex WelcomeAlex Bye Alex."

    s = input("Enter the text (or press Enter to use sample): ").strip()
    if not s:
        s = sample

    name = input("Enter the name to count (default 'Alex'): ").strip()
    if not name:
        name = "Alex"

    cnt = count_name_occurrences(s, name)
    print(cnt)


if __name__ == "__main__":
    main()
