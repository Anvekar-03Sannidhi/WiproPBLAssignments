def even_numbers(nums):
    """Return a list of even numbers from the given iterable nums."""
    return [x for x in nums if x % 2 == 0]


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(even_numbers(sample))
