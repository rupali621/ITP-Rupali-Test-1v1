pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

PENNY= 1
NICKEL= 5
DIME= 10
QUARTER = 25
DOLLAR = 100

Totalcents = (pennies * PENNY) + (nickels * NICKEL) + 
              (dimes * DIME) + (quarters * QUARTER)


Totaldollars = total_cents / DOLLAR

if Totaldollars > 1.0:
    print("result is more than 1 dollar-sorry")
if Totaldollars < 1.0:
    print("result is less than 1 dollar-sorry")

else:

    print(" WOW You are the winner")
