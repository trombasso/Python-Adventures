print("\nWhat do you need?\n-------------------")
print("1) Voltage (U)\n2) Current (I)\n3) Resistance (R)\n\n9) Quit")

loop = True
while loop is True:
    ohms_law = float(input("Please enter your choice: "))

    if ohms_law == 1: #Voltage
        current = float(input("Enter current (I): "))
        resistance = float(input("Enter resistance (R): "))
        print(f"\nThe voltage is: {current * resistance:.2f} V\n")
        continue
    elif ohms_law == 2: #Current
        voltage = float(input("Enter voltage (U): "))
        resistance = float(input("Enter resistance (R): "))
        print(f"\nThe current is: {voltage / resistance:.2f} A\n")
        continue            
    elif ohms_law == 3: #Resistance
        voltage = float(input("Enter voltage (U): "))
        current = float(input("Enter current (I): "))
        print(f"\nThe resistance is: {voltage / current:.2f} Ohms\n")
        continue    
    elif ohms_law == 9:
        loop = False
        print("Bye, Se you later!\n")
    else:
        print("Error, wrong entry. try again\n")
        continue
   

