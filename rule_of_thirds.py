import os

def rule_of_thirds(A, B, C):
    D = (C * B) / A
    return D

while True:
    try:
        # Get A, B and C values
        A = float(input("Enter the value of A: "))
        B = float(input("Enter the value of B: "))
        C = float(input("Enter the value of C: "))

        # Verify if value is different from zero
        if A == 0 or B == 0 or C == 0:
            print("Error: at least one of the values ​​entered is equal to zero. Please try again.")
            continue

        # Calculate the D's value using the rule_of_thirds
        D = rule_of_thirds(A, B, C)

        # Print the result
        print("The value of D is:", D)

    except ValueError:
        # If user types something wrong, print this error message
        print("Error: one or more values ​​entered are not numeric. Please try again.")
        continue

    # Ask if the user wants to continue or quit the program
    restart = input("Do you want to restart the program? (y/n):")

    if restart.lower() == "y" or "Y":
        # Clear the screen to restart the program
        os.system("cls" if os.name == "nt" else "clear")
    else:
        break
