import math
# This program will help users to calculate the interest on an investment either simple or compound. It will also help to calculate the amount to repay on a home loan per month.
# Asking user to choose between 'investment' and 'bond'. Making use of the lower() to avoid errors when user input in different characters


choice = input(
    "\nChoose either 'investment' or 'bond' from the menu to proceed:").lower()

print("\ninvestment - to calculate the amount of interest you'll earn on your investment.")
print("bond       - to calculate the amount you'll have to pay on a home loan.")


# Declaring variables,casting them and calculation of interest using a nested if statement.
# When user chooses 'investment'

if choice == "investment":

    amount_money = float(input("\nEnter the amount you are depositing:"))

    interest_rate = float(input("Enter your interest rate:"))

    duration = int(input("Enter the number of years for the investment:"))

    interest = input("Choose between 'simple' and 'compound':")

    if interest == "simple":
        total_amount1 = amount_money * (1 + interest_rate/100 * duration)
        print(f"\nThe total amount you will get paid is {total_amount1} ")

    elif interest == "compound":
        total_amount2 = amount_money * \
            math.pow((1+interest_rate/100), duration)
        print(f"\nThe total amount you will paid is {total_amount2}")

 # When user chooses 'bond'.

elif choice == "bond":
    house_value = float(input("\nEnter the current value of the house:"))
    bond_rate = float(input("Enter the interest rate:"))
    repay_time = int(input("Enter the number of months to repay the bond:"))

    bond_repay = round(((bond_rate*0.01)/12*house_value) /
                       (1 - math.pow(1 + ((bond_rate*0.01)/12), -repay_time)), 2)
    print(f"\nYour monthly bond repayment will be {bond_repay}")

else:
    print("\nInvalid entry. Please choose 'investment' or 'bond'.")
