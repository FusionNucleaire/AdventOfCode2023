colors =	{
  "red": 12,
  "green": 13,
  "blue": 14
}

sum = 0
with open("input") as file:
    for line in file:
        info_game = line.split(':')[0]
        info_entrees = line.split(':')[1]
        game_id = info_game[5::].strip()
        print("Game number : ", game_id)
        game_ok = True
        for entree in info_entrees.strip().split(';'):
            #print(entree)
            for game in entree.split(','):
                # is the game possible ?
                #print('game : ', game)
                number_dice = game.strip().split(' ')[0]
                color_dice = game.strip().split(' ')[1]
                if int(colors.get(color_dice)) < int(number_dice):
                    game_ok = False
                    break
        if game_ok:
            sum += int(game_id)
        print(sum)