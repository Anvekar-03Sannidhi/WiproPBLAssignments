def main():
	people = {
		"Jeff": "Is afraid of Dogs.",
		"David": "Plays the piano.",
		"Jason": "Can fly an airplane."
	}

	print("Sample output:\n")
	for name, fact in people.items():
		print(f"{name}: {fact}")
	print()

	people["Jeff"] = "Is afraid of heights."

	people["Jill"] = "Can hula dance."

	print("Updated output:\n")
	for name, fact in people.items():
		print(f"{name}: {fact}")


if __name__ == "__main__":
	main()

