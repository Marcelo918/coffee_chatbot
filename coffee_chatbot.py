"""
Author: Marcelo Villalobos Diaz
Description: This is a simple project to simulate a chat bot
"""

#Coffee Bot Function
def coffee_bot():
    print("Welcome to the cafe!")
    size = get_size()
    print(size)

    drink_type = get_drink_type()
    print(drink_type)

    print("Alright, that's a {} {}!".format(size, drink_type))

    name = input("Can I get your name please? ")
    print("Thanks, {}! Your drink will be ready shortly.".format(name))

#This message prints when the user selects a non-valid option
def print_message():
  print("I'm sorry, I did not undertand your selection. Please enter the corresponding letter for your response.")

#Function asks the user for what kind of milk they want in the latte
def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n")
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

#Function that asks the user for the size of the coffee
def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n")
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

#Function that asks the user for what type of drink they want
def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

#Calling the coffee_bot function
coffee_bot()