#!/usr/bin/env python

import sys
import random

# enemy

emHP = 50
eATK = 9
eDEF = 4
# hero
hmHP = 100
hMHP = 100
hATK = 10
hDEF = 5


def display_options():
    print('Welcome to a basic text battle\nWhat would you like to do?\n1 - Fight | 2 - Quit\n')
    user_choice = input()
    if user_choice in ['1', '2']:
        if user_choice == '2':
            sys.exit('Goodbye!')
        if user_choice == '1':
            print('A monster attacks you!')
            battle_handler()
    else:
        print('Invalid option...')


def battle_handler():
    check_state()
    print('What would you like to do?\n1-Attack | 2-Quit\n')
    user_choice = input()
    if user_choice in ['1','2']:
        if user_choice == '2':
            sys.exit('Goodbye!')
        if user_choice == '1':
            print('You attack!')
            damage_total = hATK - eDEF + random.randint(0, 10)
            print('Your attack deals ' + damage_total + ' damage!\n')
            emHP -= damage_total
            enemy_turn()


def check_state():
    if emHP <= 0 or hmHP <= 0:
        if emHP <= 0:
            win()
        if hmHP <= 0:
            lose()


def enemy_turn():
    print('The enemy attacks!')
    damage_total = eATK - hDEF + random.randint(0, 10)
    print('Their attack does ' + damage_total + ' to you!\n')
    hmHP -= damage_total


def win():
    print('You win!')


def lose():
    print('Game over man!')


def main():
    while True:
        display_options()


main()
