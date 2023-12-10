scratchcards = []

with open('input') as file:
	number_line = 0
	for line in file:
		number_line += 1
		parts = line.split('|')
		numbers_to_examine = parts[0].split(':')[1].strip().split(' ')
		winning_numbers = parts[1].strip().split(' ')
		scratchcards.append(number_line)

		# constituer l'ensemble de valeurs
		number_to_add = number_line
		ensemble_a_rajouter = []
		for number in numbers_to_examine:
			if number.isdigit() and number in winning_numbers:
				number_to_add += 1
				ensemble_a_rajouter.append(number_to_add)
				
		# pour chaque fois que la valeur number_line est trouvée, rajouter ensemble_a_rajouter
		nombre_occurrences_numero_ligne = scratchcards.count(number_line)
		ensemble = list(range(1, nombre_occurrences_numero_ligne + 1))
		
		for _ in list(range(1, nombre_occurrences_numero_ligne + 1)):
			scratchcards.extend(ensemble_a_rajouter)


print(len(scratchcards))