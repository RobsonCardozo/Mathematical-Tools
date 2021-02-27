#Ohm's Law program

result = float(); volts = float(); resistance = float(); amperes = float()

choice = int(input("1: for Voltage\n""2: for Resistance\n""3: for Current\n"": "))

if choice == 1:
    resistance = float(input ("Enter resistance in Ohms: "))
    amperes = float(input ("Enter current in amperes: "))
    result = resistance * amperes
    print(result, 'Volts')

elif choice == 2:
    volts = float(input ("Enter voltage in volts: "))
    amperes = float(input ("Enter current in amperes: "))
    result = volts / amperes
    print(result, 'Ohms')

elif choice == 3:
    volts = float(input ("Enter voltage in volts: "))
    resistance = float(input ("Enter resistance in Ohms: "))
    result = volts / resistance
    print(result, 'Amperes')

else: 
    choice = int(input("1: for Voltage\n""2: for Resistance\n""3: for Current\n"": "))