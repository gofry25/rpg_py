import random
import time
game = True
over = False
mapp = True
enemies_defeated = 0
HERO = {
    'Name': '',
    'Health':100,
    'Inventory':{
        "Sword":25,
        'Health Flask':30,
        'Health Flask Count': 3
    },
    'Armor':25,
    'Model':'🎸',
    'Base damage':10,
    'Luck':random.randint(0,6),
    'Position':[0,0]
}

ENEMY = {
    'Health':125,
    'Inventory':{
        "Бейджик":35,
        'Health Flask':30,
        'Health Flask Count': 2
    },
    'Armor':10,
    'Model':'💀',
    'Base damage':13,
    'Luck':random.randint(0,6),
    'Pos':[0,0]
}

#статы героев

HERO['Name'] = input('Назовите своего героя ->')
HEALTH_HERO = HERO['Health'] + (HERO["Armor"]*0.25)
DAMAGE_HERO = HERO['Inventory']['Sword'] + HERO["Base damage"]

HEALTH_ENEMY = ENEMY['Health'] + (ENEMY["Armor"]*0.25)
DAMAGE_ENEMY = ENEMY['Inventory']['Бейджик'] + ENEMY["Base damage"]




# MAP = [
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
# ]
# counter_hero = 0
# counter_enemies = 0
# while True:
#     while counter_hero != 1 and counter_enemies != 3:
#         for y in range(5):
#             for x in range(5):
#                 if random.randint(1,50) in [10,25,50,20,30,35]:
#                     if random.randint(0,1) == 1:
#                         if counter_hero < 1:
#                             MAP[y][x] = HERO['Model']
#                             HERO['Position'] = [y,x]
#                             counter_hero += 1
#                     else:
#                         if counter_enemies < 4:
#                             MAP[y][x] = ENEMY['Model']
#                             ENEMY['Pos'] = [y,x]
#                             counter_enemies += 1

#     while mapp == True:

#         for i in MAP:
#             print('\n')
#             for j in i:
#                 print(''.join(str(j)), end = '\t')

#         move = input("Выберите действие \n 1)Сходить направо \n 2)Сходить налево \n 3)Сходить вверх \n 4)Сходить вниз\n ->")
#         if move =='1':
#             temp = HERO['Position']
#             if temp[1] < 4:
#                 MAP[temp[0]][temp[1]] = 0
#                 MAP[temp[0]][ temp[1]+1] = HERO['Model']
#                 HERO['Position'] = [temp[0],temp[1]+1]
#         elif move == '2':

#             temp = HERO['Position']
#             if temp[1] > 0:
#                 MAP[temp[0]][temp[1]] = 0
#                 MAP[temp[0]][temp[1] - 1] = HERO['Model']
#                 HERO['Position'] = [temp[0], temp[1]- 1]
#         elif move == '3':
#             temp = HERO['Position']
#             if temp[0] > 0:
#                 MAP[temp[0]][temp[1]] = 0
#                 MAP[temp[0] - 1][temp[1]] = HERO['Model']
#                 HERO['Position'] = [temp[0] - 1, temp[1]]
#         elif move == '4':
#             temp = HERO['Position']
#             if temp[0] < 4:
#                 MAP[temp[0]][temp[1]] = 0
#                 MAP[temp[0] + 1][temp[1]] = HERO['Model']
#                 HERO['Position'] = [temp[0] + 1, temp[1]]
#     hero_pos = HERO['Position']
#     radar = ENEMY['Pos']
#     print(radar)
#     print(HERO['Position'])
#     if [radar[0]+1, radar[1]] == [hero_pos[0], hero_pos[1]]:
#         mapp == False
#         game == True

while game == True:
        HERO['Luck'] = random.randint(0, 6)
        ENEMY["Luck"] = random.randint(0, 6)
        if random.randint(1, 6) in [2, 6, 1]:
            if ENEMY['Luck'] < 3:
                ENEMY["Health"] -= DAMAGE_HERO
                ENEMY['Armor'] = ENEMY["Armor"] - ENEMY['Armor'] * 0.25
                print('Вы нанесли противнику ' + str(DAMAGE_HERO) + ' единиц урона')
            elif ENEMY['Luck'] > 2 and ENEMY["Luck"] < 5:
                ENEMY["Health"] -= DAMAGE_HERO // 3
                ENEMY['Armor'] = ENEMY["Armor"] - ENEMY['Armor'] * 0.0
                print("Противник отразил часть урона")
                print('Вы нанесли противнику ' + str(DAMAGE_HERO // 3) + ' единиц урона')
            elif ENEMY['Luck'] > 4:
                print('Противник парировал ваш удар')

        else:
            if HERO['Luck'] < 3:
                HERO["Health"] -= DAMAGE_ENEMY
                HERO['Armor'] = HERO["Armor"] - HERO['Armor'] * 0.25
                print('Противник нанёс вам ' + str(DAMAGE_ENEMY) + ' единиц урона')
            elif HERO['Luck'] > 2 and HERO["Luck"] < 5:
                HERO["Health"] -= DAMAGE_ENEMY // 3
                HERO['Armor'] = HERO["Armor"] - HERO['Armor'] * 0.0
                print("Вы отразили часть урона")
                print('Противник нанёс вам ' + str(DAMAGE_ENEMY // 3) + ' единиц урона')
            elif HERO['Luck'] > 4:
                print('Вы парировали удар врага')

        model_health = '❤'
        HEALTH_BAR_HERO = HERO["Health"] // 10
        HEALTH_BAR_ENEMY = ENEMY["Health"] // 10
        BAR_HERO = f'{HERO["Name"]}\n{HEALTH_BAR_HERO * model_health}\n'
        BAR_ENEMY = f'ENEMY\n{HEALTH_BAR_ENEMY * model_health}\n'
        print(BAR_HERO, BAR_ENEMY)
        time.sleep(2)

        if HERO["Health"] <= 0:
            print('Вы проиграли')
            game = False
            over = True
            print("Вы победили "+str(enemies_defeated)+" врагов")

        else:
            pass
        if ENEMY["Health"] <= 0:
            print('Вы победили!')
            enemies_defeated += 1
            HERO['Inventory']["Health Flask Count"] += 3 + enemies_defeated
            if HERO['Health'] <= 50:
                HERO['Health'] = random.randint(40,60)
            ENEMY['Inventory']["Health Flask Count"] = 2
            ENEMY['Health'] = 125
            cont = input("Хотите продолжить?(да/нет)")
            if cont == "да":
                pass
            else:
                game == False
                print("Вы победили "+str(enemies_defeated)+" врагов")
            
        else:
            pass

        if over == False:
            # if HERO["Health"] <= 20:
            if HERO["Inventory"]["Health Flask Count"] > 0:
                ans = input(
                    "Зелий осталось:" + str(HERO['Inventory']['Health Flask Count']) + ". Хотите вылечиться? (+/-)")
                if ans == "+":

                    HERO["Inventory"]["Health Flask Count"] -= 1
                    if HERO['Health'] <= 69:
                        HERO["Health"] += 30
                        print("Вы выпили зелье и восполнили здоровье на 30. \n")
                    else:
                        HERO['Health'] = 100
                        print("Ваше здоровье полностью восстановлено")

                    HEALTH_BAR_HERO = HERO["Health"] // 10
                    HEALTH_BAR_ENEMY = ENEMY["Health"] // 10
                    BAR_HERO = f'{HERO["Name"]}\n{HEALTH_BAR_HERO * model_health}\n'
                    BAR_ENEMY = f'ENEMY\n{HEALTH_BAR_ENEMY * model_health}\n'
                    print(BAR_HERO, BAR_ENEMY)
                    time.sleep(2)

            else:
                print('Вам нечем лечиться \n')
                time.sleep(1)
            # else:
            # pass

            if ENEMY["Health"] <= 20:
                if ENEMY["Inventory"]["Health Flask Count"] > 0:
                    ENEMY["Inventory"]["Health Flask Count"] -= 1
                    ENEMY["Health"] += 30
                    print("Враг восполнил своё здоровье на 30.")
                    HEALTH_BAR_HERO = HERO["Health"] // 10
                    HEALTH_BAR_ENEMY = ENEMY["Health"] // 10
                    BAR_HERO = f'{HERO["Name"]}\n{HEALTH_BAR_HERO * model_health}\n'
                    BAR_ENEMY = f'ENEMY\n{HEALTH_BAR_ENEMY * model_health}\n'
                    print(BAR_HERO, BAR_ENEMY)
                    time.sleep(2)
                else:
                    pass
            else:
                pass
            # else:
            #     pass

        time.sleep(2)