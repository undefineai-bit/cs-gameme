# Битва с монстром
import random
def attack(monster_hp):
    damage = random.randint(10, 25)
    monster_hp -= damage

    if monster_hp < 0:
        monster_hp = 0
    print("Вы нанесли монстру", damage, 'урона!')
    return monster_hp

def monset_attack(player_hp):
    damage = random.randint(5, 20)
    player_hp -= damage

    if player_hp < 0:
        player_hp = 0
    print("Монстр нанес вам", damage, 'урона!')
    return player_hp

def heal(player_hp):
    if player_hp == 100:
        print('Здоровье уже полное!')
    else:
        player_hp = min(player_hp + 15, 100)
        print('Вы всотановили здоровье')
    return player_hp

def show_status(player_hp, monster_hp):
    print('Ваше здоровье :', player_hp)
    print('Ваше здоровье :', monster_hp)

def main():
    player_hp = 100
    monster_hp = 100
    while player_hp > 0 and monster_hp > 0 :
        print('\nБИТВА С МОНСТРОМ')
        print('1 - Атаковать')
        print('2 - Восстановить здоровье')
        print('3 - Посмотреть состояние здоровья')
        print('4 - Выйти из игры')
        
        choise = input('\tВыберите действие:')

        if choise == '1':
            monster_hp = attack(monster_hp)
            if monster_hp > 0:
                player_hp = monset_attack(player_hp)
        elif choise == '2':
            old_hp = player_hp
            player_hp = heal(player_hp)
            if player_hp > old_hp:
                monster_hp_check = monset_attack(player_hp)
                player_hp = monster_hp_check
        elif choise == '3':
            show_status(player_hp, monster_hp)
        elif choise == '4':
            print('Вы вышлииз игры')
            
        else:
            print('Неверная команда, выберите значение от 1 до 4')
        

    if player_hp <= 0:
        print('Вы проиграли! Монстр победил')
    elif monster_hp <= 0:
        print('Вы победили!')

main()
    