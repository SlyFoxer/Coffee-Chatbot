# Error message for incorrect user input
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

# Drink type function
def get_drink_type():
  while True:
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n[d] Tea \n> ')

    if res == 'a':
      return order_brewed_coffee()
    elif res == 'b':
      return order_mocha()
    elif res == 'c':
      return order_latte()
    elif res == 'd':
      return order_tea()
    print_message()

# Drink size function  
def get_size():
  while True:
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
    if res == 'a':
      return 'small'
    elif res == 'b':
      return 'medium'
    elif res == 'c':
      return 'large'
    print_message()

# Latte milk option function
def order_latte():
  while True:
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

    if res == 'a':
      return 'latte'
    elif res == 'b':
      return 'non-fat latte'
    elif res == 'c':
      return 'soy latte'
    print_message()

# Mocha options function
def order_mocha():
  while True:
    res = input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time \n> ")
    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
    print_message()
  
# Brewed coffee options function
def order_brewed_coffee():
  while True:
    res = input("How would you like your coffee? \n[a] Black \n[b] With cream \n[c] With sugar \n[d] With cream and sugar \n> ")

    if res == 'a':
      return 'black coffee'
    elif res == 'b':
      return 'coffee with cream'
    elif res == 'c':
      return 'coffee with sugar'
    elif res == 'd':
      return 'coffee with cream and sugar'
    print_message()

# Tea options function
def order_tea():
  while True:
    res = input("What type of tea would you like? \n[a] Earl Grey \n[b] Pumpkin Spice \n[c] Vanilla \n[d] Raspberry \n[e] Apple Cinnamon \n> ")

    if res == 'a':
      return 'Earl Grey tea'
    elif res == 'b':
      return 'pumpkin spice tea'
    elif res == 'c':
      return 'vanilla tea'
    elif res == 'd':
      return 'raspberry tea'
    elif res == 'e':
      return 'apple cinnamon tea'
    print_message()

# Cup holder function
def cup_holder():
  while True:
    res =  input("Would you like a cup holder? (y/n) \n> ")

    if res == 'y':
      return 'Ok, we\'ll put your drinks in a cup holder.'
    elif res == 'n':
      return 'Ok, we won\'t put your drinks in a cup holder.'
    print_message()

# Ice question function
def ice():
  return input("Would you like ice with your drink? (y/n) \n> ")
