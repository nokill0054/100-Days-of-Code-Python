
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n"))

tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))

people_bill = int(input("Each person should pay\n"))

people_bill1 = round(float((bill+((bill*tip)/100))/people_bill),2)
print(f"Each person should pay: ${people_bill1}")               




