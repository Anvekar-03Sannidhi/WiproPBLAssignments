def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def main():
    try:
        value = input("Enter a number: ").strip()
        n = int(value)
        if is_prime(n):
            print(f"{n} is prime.")
        else:
            print(f"{n} is not prime.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == '__main__':
    main()
