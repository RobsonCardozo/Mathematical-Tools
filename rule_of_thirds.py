#crescent (basic) state of rule of thirds

left_n = float(input("Enter top left number: "))
right_n = float(input ("Enter top right number: "))
question = float(input ("Enter number in question: "))
mult = float()
x = float()

mult = (right_n * question)
x = (mult / left_n)

print(x)