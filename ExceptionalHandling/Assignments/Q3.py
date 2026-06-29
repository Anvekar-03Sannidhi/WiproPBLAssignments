def main():
    filename = input("Enter filename to open: ").strip()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        print(content.title())
    except FileNotFoundError:
        print("Error: File does not exist.")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == '__main__':
    main()
