print("*********** Welcome to Tip Calculator ***********")

bill = float(input("What was the total bill? "))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

tip_per = 1 + tip/100

final_bill = round((bill/people) * tip_per, 2)

print(f"Each person should pay: ${final_bill}")