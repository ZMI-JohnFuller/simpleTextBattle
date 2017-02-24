#!/usr/bin/env python

import sys
import random

# enemy
emHP = 50
eATK = 9
eDEF = 4
eDEX = 5
# hero
hmHP = 100
hMHP = 100
hATK = 10
hDEF = 5
hDEX = 5


def display_options():
    print('Welcome to a basic text battle\nWhat would you like to do?\n1 - Fight | 2 - Quit\n')
    user_choice = input()
    if user_choice in [1,2]:
        if user_choice == 2:
            sys.exit('Goodbye!')
        if user_choice == 1:
            print('A monster attacks you!')
            battle_handler()
    else:
        print('Invalid option...')


def battle_handler():
    check_state()
    if False:
        print('Game over man!')
        input('Enter any key to continue')
        display_options()
    elif True:
        print('HERO HP:' + str(hmHP) + '/' + str(hMHP) + '\nWhat do you want to do? \n[1]-ATTACK | [2]-QUIT\n')
        user_choice = input()
        if user_choice == 2:
            display_options()
        if user_choice == 1:
            damage_handler()


def damage_handler(damage_total):
    rand_dodge = random.randint(0, 100)
    rand_dmg = random.randint(0,10)
    if rand_dodge < 10:
        ('The attack missed!')
    else:
        damage_total -= hATK - eDEF + rand_dmg
        print ('The attack hit for ' + damage_total + ' damage!\n')
        check_state(damage_total, 0)


def check_state(emHP,hmHP):

    if emHP > 0:
        if hmHP > 0:
            if eDEX > hDEX:
                enemy_turn()
            else:
                return True
        else:
            return False
    else:
        return False

def enemy_turn():
    d

def main():
    while True:
        display_options()


main()
