dict_seeds = {}

list_seeds = []
list_seed_to_soil = []
list_soil_to_fertilizer = []
list_fertilizer_to_water = []
list_water_to_light = []
list_light_to_temperature = []
list_temperature_to_humidity = []
list_humidity_to_location = []

cursor = ''

destination_values = []
source_values = []

with open('input') as file:
    for line in file:
        if line.strip() == '':
            continue

        if line.startswith('seeds'):
            cursor = 'seeds'
            values = line.split(':')[1]
            temp = []
            for value in values.strip().split(' '):
                temp.append(value)
            dict_seeds['seeds'] = temp

        elif line[0].isalpha():
            cursor = line.split(':')[0]

        else:
            line_values = line.strip().split(' ')
            if dict_seeds.get(cursor) == None:
                dict_seeds[cursor] = [line_values]
            else:
                temp = dict_seeds.get(cursor)
                temp.append(line_values)
                dict_seeds[cursor] = temp

for seed in dict_seeds["seeds"]:
    print('---------------\ncurrent seed : '+str(seed))
    result = seed #default choice
    for soil in dict_seeds["seed-to-soil map"]:
        if int(seed) >= int(soil[1]) and int(seed) <= int(soil[1]) + int(soil[2]) - 1:
            result = int(soil[0]) + int(seed) - int(soil[1])
    
    list_seeds.append(int(seed))
    list_seed_to_soil.append(int(result)) # ok

for soil in list_seed_to_soil:
    result = soil #default choice
    for fertilizer in dict_seeds["soil-to-fertilizer map"]:
        if int(soil) >= int(fertilizer[1]) and int(soil) <= int(fertilizer[1]) + int(fertilizer[2]) - 1:
            result = int(fertilizer[0]) + int(soil) - int(fertilizer[1])

    list_soil_to_fertilizer.append(int(result)) #ok

for fertilizer in list_soil_to_fertilizer:
    result = fertilizer #default choice
    for water in dict_seeds["fertilizer-to-water map"]:
        if int(fertilizer) >= int(water[1]) and int(fertilizer) <= int(water[1]) + int(water[2]) - 1:
            result = int(water[0]) + int(fertilizer) - int(water[1])

    list_fertilizer_to_water.append(int(result))

for water in list_fertilizer_to_water:
    result = water #default choice
    for light in dict_seeds["water-to-light map"]:
        if int(water) >= int(light[1]) and int(water) <= int(light[1]) + int(light[2]) - 1:
            result = int(light[0]) + int(water) - int(light[1])

    list_water_to_light.append(int(result))

for light in list_water_to_light:
    result = light #default choice
    for temperature in dict_seeds["light-to-temperature map"]:
        if int(light) >= int(temperature[1]) and int(light) <= int(temperature[1]) + int(temperature[2]) - 1:
            result = int(temperature[0]) + int(light) - int(temperature[1])

    list_light_to_temperature.append(int(result))

for temperature in list_light_to_temperature:
    result = temperature #default choice
    for humidity in dict_seeds["temperature-to-humidity map"]:
        if int(temperature) >= int(humidity[1]) and int(temperature) <= int(humidity[1]) + int(humidity[2]) - 1:
            result = int(humidity[0]) + int(temperature) - int(humidity[1])

    list_temperature_to_humidity.append(int(result))

for humidity in list_temperature_to_humidity:
    result = humidity #default choice
    for location in dict_seeds["humidity-to-location map"]:
        if int(humidity) >= int(location[1]) and int(humidity) <= int(location[1]) + int(location[2]) - 1:
            result = int(location[0]) + int(humidity) - int(location[1])

    list_humidity_to_location.append(int(result))

print(list_seeds)
print(list_seed_to_soil)
print(list_soil_to_fertilizer)
print(list_fertilizer_to_water)
print(list_water_to_light)
print(list_light_to_temperature)
print(list_temperature_to_humidity)
print(list_humidity_to_location)

print(min(list_humidity_to_location))