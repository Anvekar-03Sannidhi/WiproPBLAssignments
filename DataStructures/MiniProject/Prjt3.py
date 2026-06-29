def average_percentage(records, name):
	
	marks = records.get(name)
	if not marks:
		return None
	return sum(marks) / len(marks)


def main():
	records = {
		"Krishna": [67, 68, 69],
		"Arjun": [70, 98, 63],
		"Malika": [52, 56, 60]
	}

	name = input("Enter a name (or press Enter to use 'Malika'): ").strip()
	if not name:
		name = "Malika"

	avg = average_percentage(records, name)
	if avg is None:
		print("Student not found or has no marks.")
	else:
		if float(avg).is_integer():
			print(f"Average percentage mark: {int(avg)}")
		else:
			print(f"Average percentage mark: {avg:.2f}")


if __name__ == "__main__":
	main()

