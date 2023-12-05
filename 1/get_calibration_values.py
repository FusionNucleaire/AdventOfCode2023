with open("input") as my_file:
	lines = my_file.readlines()
	all_numbers = []
	for line in lines:
		res = list()
		for letter in line:
			if letter in [str(x) for x in range(1, 10) if x in range(1, 10)]:
				res.append(letter)
		two_values = []
		two_values.append(int(res[0]))
		if two_values.count == 1:
			two_values.append(int(res[0]))
		else:
			two_values.append(int(res[-1]))
		all_numbers.append(two_values[0]*10 + two_values[1])
	#print(all_numbers)
	print(sum(all_numbers))