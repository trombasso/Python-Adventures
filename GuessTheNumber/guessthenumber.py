from ast import Num
import random
from os import system, name

player_tries = 0
comp_tries = 0
player = 1
high_var = 1000
low_var = 1
numb = 0


def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


comp_guess = 0
player_guess = 0


def message(x):
    if x == 1:
        print("----------------------------------------------------             \n")
        print(f"        To many guesses. The number was {numb}.                 \n")
        print("----------------------------------------------------             \n")
    if x == 2:
        print("----------------------------------------------------             \n")
        print("         G U E S S    T H E    N U M B E R                       \n")
        print("----------------------------------------------------           \n\n")
        print(f"     I've hidden a number between {low_var} and {high_var}.       ")
        print("      You have ten tries to guess my number.                       ")
        print("  If you win, you get to se me sweat...Good Luck!                \n")
        print("----------------------------------------------------             \n")
    if x == 3:
        print("----------------------------------------------------             \n")
        print(f"          Congratulations, {player_guess} is correct!           \n")
        print("------------------ L E V E L   II ------------------           \n\n")
        print("          Now you get to se how I do ;)                            ")
        print(f"  You needed {player_tries} tries, are you better than me?        ")
        print(f"      Think of a number between {low_var} and {high_var}.         ")
        print("       Follow the instructions, Have Fun!!                       \n")
        print("----------------------------------------------------             \n")
    if x == 4:
        print("------- Y O U  A R E  T H E   W I N N E R ! --------             \n")
        print("             You are superiour to me :(                            ")
        print("----------------------------------------------------             \n")
    if x == 5:
        print("----------------------------------------------------             \n")
        print("           The computer is the  b e s t !                        \n")
        print("--------------- G A M E   O V E R ------------------             \n")
    if x == 6:
        print("----------------------------------------------------             \n")
        print("       You don't get to se me sweat. Haha!                       \n")
        print("--------------- G A M E   O V E R ------------------             \n")
    if x == 7:
        print("----------------------------------------------------             \n")
        print("                    It's a tie!                                    ")
        print("--------------- W E  A L L   W I N -----------------             \n")
    if x == 8:
        print("----------------------------------------------------             \n")
        print(f"                Your number is {comp_guess}.                    \n")
        print(f"        I've had {comp_tries} tries against your {player_tries}.\n\n")


def main():
    global player
    global player_tries
    global numb
    global player_guess

    clear()
    message(2)
    numb = random.randint(low_var, high_var)
    tries = 10

    while player_guess < numb or player_guess > numb:
        while tries >= 1:
            try:
                player_guess = int(input(f"Make a guess: "))
            except ValueError:
                print("Not a valid input, try again.")
            else:
                break

        if player_guess < low_var or player_guess > high_var:
            print(f"Enter a number between {low_var}-{high_var}")
        elif player_guess < numb and tries >= 1:
            print(f"To low. {tries-1} tries left.")
            tries -= 1
        elif player_guess > numb and tries >= 1:
            print(f"To high. {tries-1} tries left.")
            tries -= 1
        elif player_guess == numb:
            # print(f"\n\nCongratulations, you guessed correctly!\n\n")
            tries -= 1
            player = 1
            break
        elif tries == 0:
            message(1)
            player = 0
            break

    player_tries = 10 - tries


def computer_guess():

    global comp_tries
    global comp_guess
    global low_var
    global high_var
    low_numb = low_var
    high_numb = high_var
    comp_guess = random.randint(low_var, high_var)
    comp_tries = 0

    message(3)
    input("Hit enter when ready...")
    while True:
        if (
            (low_numb == high_numb)
            or (comp_guess == high_numb + 1)
            or (comp_guess == low_numb - 1)
        ):
            comp_tries += 1
            message(8)
            break
        else:
            print(f"My guess is {comp_guess}!")
            player_input = input(f"Low (L) / High (H) or Correct (C): ").lower()

            if player_input == "l":
                low_numb = comp_guess + 1
                comp_guess = random.randint(low_numb, high_numb)
                comp_tries += 1
            elif player_input == "h":
                high_numb = comp_guess - 1
                comp_guess = random.randint(low_numb, high_numb)
                comp_tries += 1
            elif player_input == "c":
                comp_tries += 1
                message(8)
                break


# def computer_guess():
#     global comp_tries
#     global comp_guess
#     global low_var
#     global high_var
#     low_numb = low_var
#     high_numb = high_var
#     comp_guess = (low_numb + (high_numb -1)) // 2
#     comp_tries = 0

#     message(3)
#     input("Hit enter when ready...")
#     while True:
#         if (low_numb == high_numb) or (comp_guess == high_numb +1) or (comp_guess == low_numb -1):
#             comp_tries += 1
#             message(8)
#             break
#         else:
#             print(f"My guess is {comp_guess}!")
#             print(low_numb, high_numb)
#             player_input = input(f"Low (L) / High (H) or Correct (C): ").lower()

#             if player_input == "l":
#                 low_numb = comp_guess
#                 comp_guess = round((low_numb + (high_numb - 1)) / 2)
#                 comp_tries += 1
#             elif player_input == "h":
#                 high_numb = comp_guess
#                 comp_guess = round((low_numb + (high_numb - 1)) / 2)
#                 comp_tries += 1
#             elif player_input == "c":
#                 comp_tries += 1
#                 message(8)
#                 break


if __name__ == "__main__":
    # main()
    if player == 1:
        computer_guess()
        if comp_tries < player_tries:
            message(5)
        elif comp_tries == player_tries:
            message(7)
        else:
            message(4)
            exit()
    else:
        message(6)
