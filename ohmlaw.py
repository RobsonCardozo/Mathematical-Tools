def calculate_voltage(resistance: float, amperes: float) -> float:
    return resistance * amperes

def calculate_resistance(volts: float, amperes: float) -> float:
    return volts / amperes

def calculate_current(volts: float, resistance: float) -> float:
    return volts / resistance

def main():
    while True:
        print("Please choose an option:")
        print("1. Calculate Voltage")
        print("2. Calculate Resistance")
        print("3. Calculate Current")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "4":
            print("Exiting.")
            break

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a valid option.\n")
            continue

        if choice < 1 or choice > 3:
            print("Invalid choice. Please enter a valid option.\n")
            continue

        try:
            if choice == 1:
                resistance = float(input("Enter resistance in Ohms: "))
                amperes = float(input("Enter current in Amperes: "))
                result = calculate_voltage(resistance, amperes)
                print(f"The voltage is {result:.2f} volts.\n")
            elif choice == 2:
                volts = float(input("Enter voltage in Volts: "))
                amperes = float(input("Enter current in Amperes: "))
                result = calculate_resistance(volts, amperes)
                print(f"The resistance is {result:.2f} ohms.\n")
            elif choice == 3:
                volts = float(input("Enter voltage in Volts: "))
                resistance = float(input("Enter resistance in Ohms: "))
                result = calculate_current(volts, resistance)
                print(f"The current is {result:.2f} amperes.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            continue


if __name__ == '__main__':
    main()
