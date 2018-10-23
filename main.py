starting_home = int(input("введите номер дома откуда начинаем: "))
ending_home = int(input("введите номер дома до которого идём: "))

result = 0

if starting_home < ending_home:
    if starting_home % 2 == 0 and ending_home % 2 == 0:
        result = int((ending_home-starting_home) / 2)
    elif starting_home % 2 == 0 and ending_home % 2 != 0:
        starting_home -= 1
        result = int((ending_home - starting_home) / 2)
    elif starting_home % 2 != 0 and ending_home % 2 == 0:
        starting_home += 1
        result = int((ending_home - starting_home) / 2)
    elif starting_home % 2 != 0 and ending_home % 2 != 0:
        result = int((ending_home - starting_home) / 2)
    else:
        print("watafaaaaak")
else:
    if starting_home % 2 == 0 and ending_home % 2 == 0:
        result = int((starting_home-ending_home) / 2)
    elif starting_home % 2 == 0 and ending_home % 2 != 0:
        ending_home += 1
        result = int((starting_home - ending_home) / 2)
    elif starting_home % 2 != 0 and ending_home % 2 == 0:
        ending_home -= 1
        result = int((starting_home- ending_home) / 2)
    elif starting_home % 2 != 0 and ending_home % 2 != 0:
        result = int((starting_home - ending_home) / 2)
    else:
        print("watafaaaaak")
print(result)
