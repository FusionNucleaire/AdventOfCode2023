def find_numbers(line):
	nombres_trouves = []
	if 'one' in line:
		nombres_trouves.append(["1", line.index('one')])
		nombres_trouves.append(["1", line.rindex('one')])
	if 'two' in line:
		nombres_trouves.append(["2", line.index('two')])
		nombres_trouves.append(["2", line.rindex('two')])
	if 'three' in line:
		nombres_trouves.append(["3", line.index('three')])
		nombres_trouves.append(["3", line.rindex('three')])
	if 'four' in line:
		nombres_trouves.append(["4", line.index('four')])
		nombres_trouves.append(["4", line.rindex('four')])
	if 'five' in line:
		nombres_trouves.append(["5", line.index('five')])
		nombres_trouves.append(["5", line.rindex('five')])
	if 'six' in line:
		nombres_trouves.append(["6", line.index('six')])
		nombres_trouves.append(["6", line.rindex('six')])
	if 'seven' in line:
		nombres_trouves.append(["7", line.index('seven')])
		nombres_trouves.append(["7", line.rindex('seven')])
	if 'eight' in line:
		nombres_trouves.append(["8", line.index('eight')])
		nombres_trouves.append(["8", line.rindex('eight')])
	if 'nine' in line:
		nombres_trouves.append(["9", line.index('nine')])
		nombres_trouves.append(["9", line.rindex('nine')])
	return nombres_trouves


with open("input") as my_file:
	lines = my_file.readlines()
	all_numbers = []
	for line in lines:
		#print('-----------------------')
		#print(line)
		found_numbers_text = find_numbers(line)
		found_numbers_ints = []
		
		#print(found_numbers_text)

		for idx, letter in enumerate(line):
			if letter in [str(x) for x in range(1, 10) if x in range(1, 10)]:
				found_numbers_ints.append([letter, idx])
		#print(found_numbers_ints)
		
		all_numbers_sorted = sorted(found_numbers_text + found_numbers_ints, key=lambda x:x[1])
		#print('all_numbers_sorted', all_numbers_sorted)
		
		first_value = all_numbers_sorted[0]
		if len(all_numbers_sorted) == 1:
			last_value = all_numbers_sorted[0]
		else:
			last_value = all_numbers_sorted[-1]

		#print('valeur finale', int(first_value[0])*10 + int(last_value[0]))
		all_numbers.append(int(first_value[0])*10 + int(last_value[0]))

	#print(all_numbers)
	#print(len(all_numbers))
	print(sum(all_numbers))
