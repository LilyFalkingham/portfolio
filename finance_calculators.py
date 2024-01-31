import math

# Two financial calculators:
# Investment calc. and home loan repayment calc.
# Allow user to choose which calculation
print("\nThis program offers two calculators:")
print("\nInvestment   -   " 
      "to calculate the amount of interest you'll earn on your investment")
print("Bond         -   " 
      "to calculate the amount you'll have to pay on a home loan")

while True:
    chosen_calculator = input("\nEnter either 'investment' or 'bond' " 
                              "from the menu above to proceed: ").lower()

    # If 'investment' entered
    # Request required info from user for investment calc.
    if chosen_calculator == "investment":
        deposit = int(input("\nPlease enter the amount of money you are " 
                            "depositing in pounds (e.g. 1000): £"))
        interest_rate = int(input("Please enter the interest rate as a " 
                                  "percentage (e.g. 8): "))/100
        years_investing = int(input("Please enter the number of years " 
                                    "you plan on investing (e.g. 20): "))
        interest = input("Please enter the type of interest, 'simple' or " 
                         "'compound': ").lower() 
    
        # Depending on 'simple' or 'compound' entered:
        # Perform relevant calc. and display total return on investment
        if interest == "simple":
            simple_total = deposit * (1 + interest_rate * years_investing)
            print(f"\nYour total return on investment will be: "
                  f"£{round(simple_total, 2)}")
            break
        elif interest == "compound":
            comp_total = deposit * math.pow((1+interest_rate), years_investing)
            print(f"\nYour total return on investment will be: " 
                  f"£{round(comp_total, 2)}")
            break
        else:
            print("\nERROR: Invalid entry for type of interest. " 
                  "Please try again and enter either 'simple' or 'compound'.")

    # If 'bond' entered
    # Request required info from user 
    # Perform bond calc. and display amount to repay each month
    elif chosen_calculator == "bond":
        house_value = int(input("\nPlease enter the value of your house " 
                                "(e.g. 100000): £"))
        monthly_int_rate = int(input("Please enter the interest rate as a " 
                                     "percentage (e.g. 7): "))/100/12
        months_to_repay = int(input("Please enter the number of months you " 
                                    "plan to take to repay the bond " 
                                    "(e.g 120): "))
        
        repayment = (monthly_int_rate * house_value)/ \
                    (1-(1+monthly_int_rate)**(-months_to_repay))
        print(f"\nThe amount you will need to repay each month is: " 
              f"£{round(repayment, 2)}")
        break

    # Invalid entry for investment or bond, show error message
    else:
        print("\nERROR: Invalid entry. Please try again and enter either " 
              "'investment' or 'bond'.")
