# Day 15 making coffee machine

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
             }


def report():
    '''This give talls you about the amount of ingredient in the machine '''
    for i in resources:
        if i=="coffee":
            print(f"{i}: {resources[i]}g")
        elif i=="money":
            print(f"{i}: ${resources[i]}")
        else:
            print(f"{i}: {resources[i]}ml")

menu = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18, "milk": 0}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

def ingredients_taker(item_name):
    '''This function take sufficent amount of ingredients from resource'''
    for i in resources:
        if i=='money':
            resources[i]+=menu[item_name]['cost']
        else:
            resources[i]-=menu[item_name]['ingredients'][i]

def money_checker(item_name):
   '''This function check Whether customer have the enough money for it's item'''
   print("Please insert coins.")
   total=0
   coin_list={
       "qusrters":0.25,
       "dimes":0.10,
       "nikels": 0.05,
       "pennies": 0.01
       }

   for coin in coin_list:
       money=int(input(f"How many {coin}: "))
       money*= coin_list[coin]
       total+=money
    
   if total >= menu[item_name]["cost"]:
       return total - menu[item_name]["cost"]
   else:
       return "Money refund"
   

def checker(item_name):
    '''This function check that machine have sufficent amount ingredients or not  '''

    for i in resources:
        if i == "money":
            continue
        elif resources[i]<menu[item_name]['ingredients'][i]:
            print(f"Sorry we don't have saficient {i} for making your {item_name} 😢😢😔")
            return False
        else:
            return True
   

from Art import coffee_machine

print(coffee_machine)
machine= "on"
while machine=="on":
    customer_ask= str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if customer_ask== "off":
        print("Machine is turning off")
        machine="off"
    elif customer_ask in menu :
        availability=checker(customer_ask)
        if availability is not True:
          continue
        else:
            money=money_checker(customer_ask)
            if money=="Money refund":
                print("You don't have enough money for your order. Money is refunded")
            else:
                print(f"Here is your change ${round(money,2)}")
                print(f"Enjoy your {customer_ask} ☕☕")
                ingredients_taker(customer_ask)
    elif customer_ask== "report":
        report()
    
    else:
        print(f"You might have give wrong command '{customer_ask}' ")




