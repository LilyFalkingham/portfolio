# Continually ask user to enter number 
# If user enters '-1' stop requesting number

# Request number input
# Set up variables to count no. of  entries and sum numbers entered
number = float(input("Please enter a number, enter -1 to stop: "))
numbers_summed = 0
entries = 0

# Use while loop to sum numbers and number of entries until -1 is entered
while number != -1:
    numbers_summed += number
    entries += 1
    number = float(input("Please enter a number, enter -1 to stop: "))

# Calculate and print average of numbers entered excluding '-1'
if entries == 0:
    print("You didn't enter any numbers.")
else:
    average = round((numbers_summed/entries), 2)
    print(f"\nYou entered {entries} numbers. The average of the numbers you entered is: {average}")