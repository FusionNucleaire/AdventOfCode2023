colors =	{
  "red": 12,
  "green": 13,
  "blue": 14
}

total_power = 0
with open("input") as file:
    for line in file:
        info_game = line.split(':')[0]
        info_entrees = line.split(':')[1]
        game_id = info_game[5::].strip()
        print("------------------")
        print("Game number : ", game_id)
        game_ok = True
        red = green = blue = 0
        for entree in info_entrees.strip().split(';'):
            
            print('Entree : ', entree)
            for ligne in entree.split(','):
                
                number_dice = ligne.strip().split(' ')[0]
                color_dice = ligne.strip().split(' ')[1]
                print('Ligne : ', number_dice, color_dice)
                if str(color_dice) == 'red':
                    red = max(int(number_dice), red)
                if str(color_dice) == 'green':
                    green = max(int(number_dice), green)
                if str(color_dice) == 'blue':
                    blue = max(int(number_dice), blue)
        print('red : ',red, 'green : ',green, 'blue : ', blue)
        print('power : ', red*green*blue)
        total_power += red*green*blue
    print('total power : ', total_power)
        
