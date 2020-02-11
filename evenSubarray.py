def evenSubarray(numbers, k):
	set_of_sublists = set()
	N = len(numbers)
	for sublist_size in range(1, N + 1):
		for i in range(0, N - sublist_size + 1):
			set_of_sublists.add(tuple(numbers[i: i + sublist_size]))
	ans = len(set_of_sublists)
	for sublist in set_of_sublists:
		odds_counter = 0
		good_sublist = True
		for element in sublist:
			odds_counter += 1 if element % 2 != 0 else 0
			if odds_counter > k: ans -= 1; break
	return ans

if __name__ == '__main__':
	numbers = [1, 2, 3, 4]
	print(evenSubarray(numbers, 1))