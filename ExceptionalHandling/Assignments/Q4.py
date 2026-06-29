def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        idx = int(input("Enter an index: ").strip())
        value = numbers[idx]
        if value >= 0:
            print(f"The value at index {idx} is positive: {value}")
        else:
            print(f"The value at index {idx} is negative: {value}")
    except IndexError:
        print("Error: Invalid index entered.")
    except ValueError:
        print("Error: Please enter a valid integer index.")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == '__main__':
    main()
