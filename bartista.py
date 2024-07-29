

print("Welcome to the coffee place - we have a menu as follows-")
menu = "Black Coffee, Expresso, Cold Press, Latte, Cappucino"
print("Our Menu Today is\n" + menu + "\nWhat looks good to you")
order = input()
# Set the price for items     
if order == "Black Coffee":
    price = 13
elif order == "Expresso":
   price = 3
elif order == "Cold Press":
   price = 4
elif order == "Latte":
   print("Would you like to add whipped cream to this for $3 more? \n")
   input()
   if input == "Yes":
    price = 13
    print(print)
   else:
    price = 10
elif order == "Cappucino":
   price = 6
else:
   print("Sorry We are all out of that would you care to try " + menu)
   price = 0

quantity = input("How many would you like?\n")

total = price * int(quantity)
result = f"{quantity} {order}"
result = "{} {}".format(quantity, order)

name = input("What is your name?\n")
if name == "Ben" or name == "ben" or name == "Patricia":
  evil_status = input("Are you evil?\n")
  if evil_status == "Yes" or evil_status == "yes":  
    print("You are not welcome " + name)
    exit()
  else:
     print("OK.  You are good to go.  Thank you for your order " + name + "\nWe are putting together " + result + "\nIt will cost you $" + str(total))

else:
     print("Thank you for your order " + name + "\nWe are putting together " + result + "\nIt will cost you $" + str(total))