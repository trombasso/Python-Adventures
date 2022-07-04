from os import name, system


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


for x in range(0, 65):
    clear()
    print(f"The number {x:>2} is in binary: {x:>08b}\n\n")
    input("Press enter for next number...")
