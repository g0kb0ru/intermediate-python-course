# Python3 Project - Dice Roll
# Author: g0kb0ru
import random

player_numbers = int(input('How many players would you like to play?'))
if player_numbers == 2:
    p1 = p2 = 0
elif player_numbers == 3:
    p1 = p2 = p3 = 0
elif player_numbers == 4:
    p1 = p2 = p3 = p4 = 0
else:
    print("Choose from 2 to 4 player")
    quit()
dice_rolls = int(input('How many dice would you like to roll?'))
dice_size = int(input('How many sides are the dice? '))


for j in range(0, player_numbers):
    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_size)
        dice_sum += roll
        if roll == 1:
            print(f"Player {j+1} has rolled a {roll}! Critical Fail")
        elif roll == 6:
            print(f"Player {j+1} has rolled a {roll}! Critical Success")
        else:
            print(f"Player {j+1} rolled a {roll}")
    if j == 0:
        p1 = dice_sum
    elif j == 1:
        p2 = dice_sum
    elif j == 2:
        p3 = dice_sum
    else:
        p4 = dice_sum

if player_numbers == 2:
    print(f"Player 1 have rolled total of {p1}")
    print(f"Player 2 have rolled total of {p2}")
    if p1 > p2:
        print("Player 1 won the game!")
    elif p2 > p1:
        print("Player 2 won the game!")
    else:
        print("Draw!")
elif player_numbers == 3:
    print(f"Player 1 have rolled total of {p1}")
    print(f"Player 2 have rolled total of {p2}")
    print(f"Player 3 have rolled total of {p3}")
    if p1 > p2 and p1 > p3:
        print("Player 1 won the game!")
    elif p2 > p1 and p2 > p3:
        print("Player 2 won the game!")
    elif p3 > p1 and p3 > p2:
        print("Player 2 won the game!")
    else:
        print("Draw!")
else:
    print(f"Player 1 have rolled total of {p1}")
    print(f"Player 2 have rolled total of {p2}")
    print(f"Player 3 have rolled total of {p3}")
    print(f"Player 4 have rolled total of {p4}")
    if p1 > p2 and p1 > p3 and p1 > p4:
        print("Player 1 won the game!")
    elif p2 > p1 and p2 > p3 and p2 > p4:
        print("Player 2 won the game!")
    elif p3 > p1 and p3 > p2 and p3 > p4:
        print("Player 2 won the game!")
    elif p4 > p1 and p4 > p3 and p4 > p3:
        print("Player 2 won the game!")
    else:
        print("Draw!")


def main():
    print('The End...')


if __name__ == "__main__":
    main()
