#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this is a Rock, Paper, Scissors, Lizard and Spock
Game Simulation Module.
"""


import random


def action_to_number(action):
    """
    takes the action and return the equivalent number.
    """
    if action == "rock":
        return 0
    elif action == "Spock":
        return 1
    elif action == "paper":
        return 2
    elif action == "lizard":
        return 3
    elif action == "scissors":
        return 4
    else:
        return "q"


def number_to_action(number):
    """
    takes the number and return the equivalent action.
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "q"


def rpsls():
    """
    takes the player action and compare it to
    the computer guess action and return the winner.
    """
    player_name = input("What's your name Soldier:>")
    print(" ")
    print("Welcome", player_name)
    while True:
        player_action = input("What's your action:>")
        try:
            player_number = action_to_number(player_action)
            computer_number = random.randrange(0, 5)
            winner = (player_number - computer_number) % 5
        except:
            print(" ")
            print("Bad choice", player_action)
            break
        if player_action == "q":
            break
        print(" ")
        print(player_name, "chooses", player_action)
        print(" ")
        computer_action = number_to_action(computer_number)
        print("Computer chooses", computer_action)
        print(" ")
        if winner == 0:
            print("It's a tie, Please try again.")
        elif winner <= 2:
            print(player_name, "Win!")
        elif winner > 2:
            print("Computer Win!")
    print(" ")
    print("Thanks and goodbye, hope to see you soon!")


print(" ")
print("Welcome to the Rock, Paper, Scissors, Lizard and Spock Game.")
print(" ")
print("It's very simple")
print(" ")
print("Scissors cuts paper")
print("Paper covers rock")
print("Rock crushes lizard")
print("Lizard poisons Spock")
print("Spock smashes scissors")
print("Scissors decapitates lizard")
print("Lizard eats paper")
print("Paper disproves Spock")
print("Spock vaporizes rock")
print(" ")
print("And as it always has been")
print(" ")
print("Rock crushes scissors")
print(" ")
print("Please Choose Your Action from the list")
print("[rock, paper, scissors, lizard, Spock]")
print("or q to exit")
rpsls()
