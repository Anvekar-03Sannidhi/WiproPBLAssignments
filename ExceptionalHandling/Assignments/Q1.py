def main():
    try:
        a = float(input("Enter first number: ").strip())
        b = float(input("Enter second number: ").strip())

        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Please enter valid numbers.")

    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
