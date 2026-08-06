# data types error type checkingtype casting math operator number manipulation f string
# tip calculator
print("Welcome to the tip calculator !")
bill = float(input("What was the total bill? $"))
tip = float(input("How much percentage tip you would like to give? 10 , 12, 15? "))
bill_with_tip = tip / 100 * bill + bill
people = float(input("How many people to split the bill? "))
totalbill = bill_with_tip / people
print(totalbill)
print(type(totalbill))  # type checking
print(int(totalbill))  # type casting
