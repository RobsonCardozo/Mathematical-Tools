import os


def calculate_voltage(resistance, amperes):
    return resistance * amperes


def calculate_resistance(volts, amperes):
    return volts / amperes


def calculate_current(volts, resistance):
    return volts / resistance


def format_value(value):
    if abs(value) >= 1000:
        if abs(value) >= 1000000:
            value = value / 1000000
            suffix = "M"
        else:
            value = value / 1000
            suffix = "K"
        return f"{value:.2f} {suffix}"
    else:
        return f"{value:.2f}"


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Choose an option:")
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
            input("Invalid choice. Please enter a valid option.\nPress Enter to continue...")
            continue

        if choice < 1 or choice > 3:
            input("Invalid choice. Please enter a valid option.\nPress Enter to continue...")
            continue

        try:
            if choice == 1:
                resistance = float(input("Enter resistance in Ohms: "))
                amperes = float(input("Enter current in Amperes: "))
                result = calculate_voltage(resistance, amperes)
                print(f"The voltage is {format_value(result)} volts.")
            elif choice == 2:
                volts = float(input("Enter voltage in Volts: "))
                amperes = float(input("Enter current in Amperes: "))
                result = calculate_resistance(volts, amperes)
                print(f"The resistance is {format_value(result)} ohms.")
            elif choice == 3:
                volts = float(input("Enter voltage in Volts: "))
                resistance = float(input("Enter resistance in Ohms: "))
                result = calculate_current(volts, resistance)
                print(f"The current is {format_value(result)} amperes.")
            input("\nPress Enter to continue...")
        except ValueError:
            input("Invalid input. Please enter a valid number.\nPress Enter to continue...")
            continue


if __name__ == '__main__':
    main()
