total = 0

with open('input') as file:
    number_line = 0
    for line in file:
        total_line = 0
        to_add = 0
        multiplicator = 1
        double = False
        number_line += 1
        print('---------------')
        #print(line)
        parts = line.split('|')
        numbers_to_examine = parts[0].split(':')[1].strip().split(' ')
        winning_numbers = parts[1].strip().split(' ')
        print(numbers_to_examine)
        print(winning_numbers)
        for number in numbers_to_examine:
            if number.isdigit() and number in winning_numbers:
                if double == True:
                    multiplicator = multiplicator * 2
                else:
                    double = True
                    to_add = 1
        print(to_add * multiplicator)
        total += to_add  * multiplicator 

print(total)