print("Welcome to the coffee place - we have a menu as follows-")
menu = "Black Coffee, Espresso, Cold Press, Latte, Cappucino"
print("Our Menu Today is\n" + menu + "\nWhat looks good to you?")
order = input()

prices = {
    "Black Coffee": 1.3,
    "Espresso": 3,
    "Cold Press": 4,
    "Latte": 10,
    "Cappucino": 6
}

try:
    price = prices[order]
    if order == "Latte":
        whip_cream = input("Would you like to add whipped cream to this for $3 more? (Yes/No)\n").lower()
        if whip_cream == "yes":
            price += 3
except KeyError:
    print("Sorry, we are all out of that. Would you care to try something else from our menu?")
    price = 0

quantity = int(input("How many would you like?\n"))
name = input("What is your name?\n")
if name == "Ben" or name == "ben" or name == "Patricia":
  evil_status = input("Are you evil?\n")
  if evil_status == "Yes" or evil_status == "yes":  
    print("You are not welcome " + name)
    exit()
  else:
     print("OK.  You are good to go.")

total = price * quantity

print(f"Thank you for your order, {name}. We are putting together {quantity} {order}. It will cost you ${total:.2f}.")
