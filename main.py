#!/usr/bin/env python

import sys
import random
import winsound
import time

# enemy

emHP = 50
eMHP = 50
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
        print('Invalid option...\n')
        display_options()


def battle_handler():
    global emHP
    check_state()
    print('What would you like to do?\n1-Attack | 2-Quit\n')
    print('HP:' + str(hmHP) + '/' + str(hMHP))
    print('HP:' + str(emHP) + '/' + str(eMHP))
    user_choice = input()
    if user_choice in ['1', '2']:
        if user_choice == '2':
            quit_game()
        if user_choice == '1':
            print('You attack!')
            winsound.PlaySound('.\sword.wav', winsound.SND_ASYNC)
            damage_total = hATK - eDEF + random.randint(0, 10)
            print('Your attack deals ' + str(damage_total) + ' damage!\n')
            emHP -= damage_total
            check_state()
            time.sleep(1)
            enemy_turn()
    else:
        print('Invalid choice...\n')
        battle_handler()


def check_state():
    global emHP
    if emHP <= 0 or hmHP <= 0:
        if emHP <= 0:
            emHP = 0
            win()
        if hmHP <= 0:
            lose()


def enemy_turn():
    global hmHP
    print ('The enemy is thinking...')
    sleep_time = random.randint(1, 3)
    time.sleep(sleep_time)
    print('The enemy attacks!')
    winsound.PlaySound('.\hit.wav', winsound.SND_ASYNC)
    damage_total = eATK - hDEF + random.randint(0, 10)
    print('Their attack does ' + str(damage_total) + ' to you!\n')
    hmHP -= damage_total
    check_state()
    battle_handler()


def win():
    print('You win!')
    user_choice = input('Play again? 1- Yes | 2- No!')
    if user_choice in ['1', '2']:
        if user_choice == '2':
            quit_game()
        if user_choice == '1':
            reset_stats()
            battle_handler()
    else:
        print('Invalid input\n')


def lose():
    print('Game over man!')


def reset_stats():
    global emHP
    global hmHP
    emHP = eMHP
    hmHP = hMHP


def quit_game():
    sys.exit("Goodbye!")


def main():
    while True:
        display_options()
        time.sleep(1)


main()
