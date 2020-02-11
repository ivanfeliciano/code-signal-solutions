def firstDuplicate(a):
	INF = 10000000000
	map_duplicates = {}
	for i in range(len(a)):
		if a[i] in map_duplicates:
			if len(map_duplicates[a[i]]) > 1:
				continue
			map_duplicates[a[i]].append(i)
		else:
			map_duplicates[a[i]] = [i]
	min_duplicate_idx = INF
	for key in map_duplicates:
		if len(map_duplicates[key]) < 2:
			continue
		min_duplicate_idx = min(map_duplicates[key][1], min_duplicate_idx)
	ans = a[min_duplicate_idx] if min_duplicate_idx < INF else -1
	return ans

def main():
	a = [2,1,3,5,4]
	print(firstDuplicate(a))
if __name__ == '__main__':
	main()