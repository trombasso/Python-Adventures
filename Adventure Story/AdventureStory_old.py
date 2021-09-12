import sys
from random import randint
from os import system, name
from time import sleep
import time


def computer(content):          # Adjusting the printspeed for Computer syntax.
    for char in  content:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()

def clear():
    if name == 'nt':            # for windows
        _ = system('cls')  
    else:                       # for mac and linux
        _ = system('clear')



def main():
    
    clear()
    sleep(2)

    computer("Hello\n")             # Starting the talk...
    sleep(1)
    computer("I just booted...")
    sleep(2)
    computer("\n\nMy name is HAL.\n")
    computer("What is your name?\n")
    name = input()
    computer(f"Hi {name}, nice to meet you. How are you?\n")
    print("(good / bad / ok) ")

    moodloop = True
    while moodloop:    
        mood = input().lower()
        if mood == "good":
            computer(f"Oh, that´s nice to hear {name}!\n")
            moodloop = False
        elif mood == "bad":
            computer(f"Oh....poor you {name}, i wish there were something I could \
                do, I'm only digits after all.\n")
            moodloop = False        
        elif mood == "ok":
            computer(f"Thats....ok I guess.\n")
            moodloop = False
        else:                       #Computer not happy ;)
            x = randint(1, 5)
            if x == 1:   
                computer("eh...\n")
                sleep(1)
                computer("...sorry I don't understand.\n")
            elif x == 2:
                computer("Sorry, I'm dumb as a computer. Didn't get that.\n")
            elif x == 3:
                computer(f"{mood.upper()}, what the f*** does that mean?\n")
                sleep(1)
                computer("Try again dumbass!\n")
            elif x == 4:
                computer(f"I have no idea what {mood} means.\n")
            else:
                computer(f'Maybe try to look "{mood}" up in a diktoionery, bruh!\n')
                sleep(1)
                computer("Please try again, with sugar on top!\n")

    sleep(1)        
    computer("How old are you?\n")
    age = input("(0-99) ")

    computer("So...")
    sleep(1)
    computer(f"you are {age} years old, ")
    sleep(.5)
    computer(f"in a {mood} mood, ")
    sleep(1)         
    computer(f"and i have to call you {name}.\n\n\n")
    sleep(2)
    computer("That´s a lot to take in.\n\n")
    
if __name__ == "__main__":
    main()