print("Information for user, please read the below definitions to support your choice of calculator: ")
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan")
which_calculator = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Convert the input to lower case so that it does not matter and can compare
which_calculator_lower = which_calculator.lower()

# different variables that I will need to use
investment = "investment"
bond = "bond"
simple = "simple"
compound = "compound"

# If the user choose investment, they can then input the variable for the amount of money, interest %, number of years and the type of interest
# they will then need a choice between simple interest and compound
# The program will print the calculated amount of simple or compound interest
if which_calculator_lower == investment:
    money = int(input("Please enter the amount of money you are depositing as a number: £"))
    interest_rate = int(input("Please enter the interest rate (You do not need to include % sign): "))
    r = interest_rate / 100
    number_years = int(input("Please enter the number of years you plan on investing: "))
    while True:
        interest = input("Please enter whether you would like 'simple' or 'compound': ").lower()
        if interest == simple or interest == compound:
            break
        else:
            print("Invalid input. Please type either 'simple' or 'compound'.")

    if interest == simple:
        print("The total amount you will get back after the given period for simple interest is: £", (money * (1 + r * number_years)), "Thank you.")
    elif interest == compound:
        print("The total amount you will get back after the given period for compound interest is: £", (money * (1 + r) ** number_years), "Thank you.")
# If the user chooses bond, then the user will need to input the present value of their house, interest rate and number of months they plan to repy the bond
elif which_calculator_lower == bond:
    value_house = int(input("Please enter the current value of your house in £: "))
    interest_rate = int(input("Please enter the current interest rate (You do not need to include the % sign):"))
    months_repay = int(input("Please enter the number of months you plan to take to repay the bond: "))
    # bond repayment formula
    annual_interest_rate = (interest_rate / 100) / 12
    bond_repayment_formula = (annual_interest_rate * value_house) / (1 - (1 + annual_interest_rate) ** (-months_repay))
    print("You will have to repay the following each month: £", bond_repayment_formula, "Thank you.")
else:
    print("You have typed in an invalid response, please try again, use the word 'Investment' or 'Bond'. Thanks.")
