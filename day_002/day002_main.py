print("Welcome to the tip calculator.")
bill = None
n_people = None
while bill is None:
    try:
        bill = float(input("What was the total bill? "))
    except ValueError:
        print("Invalid value")

while n_people is None:
    try:
        n_people = int(input("How many people to split the bill? "))
    except ValueError:
        print("Invalid value")

percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
if percentage not in ['10', '12', '15']:
    while percentage not in ['10', '12', '15']:
        print("Invalid value")
        percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")

splited_bill = bill * (int(percentage) / 100 + 1) / n_people
print(f'Each person should pay: ${round(splited_bill, 2)}')
