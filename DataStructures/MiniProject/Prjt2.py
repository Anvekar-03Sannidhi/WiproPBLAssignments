def runner_up(scores):
	
	unique_scores = sorted(set(scores), reverse=True)
	if len(unique_scores) < 2:
		return None
	return unique_scores[1]


def main():

	sample = [2, 3, 6, 6, 5]

	s = input("Enter scores separated by spaces (or press Enter to use sample): ").strip()
	if s:
		try:
			scores = [int(x) for x in s.split()]
		except ValueError:
			print("Invalid input. Using sample list instead.")
			scores = sample
	else:
		scores = sample

	result = runner_up(scores)
	if result is None:
		print("No runner-up score found.")
	else:
		print(result)


if __name__ == "__main__":
	main()

