import random
def name_to_number(name):
    if name== 'Rock':
        return 0
    elif name== 'Spock':
        return 1
    elif name== 'Paper':
        return 2
    elif name== 'Lizard':
        return 3
    elif name== 'Scissors':
        return 4
    else: "Error"
def number_to_name(number):
      if number == 0:
        return 'Rock'
      elif number== 1:
        return 'Spock'
      elif number== 2:
        return 'Paper'
      elif number== 3:
        return 'Lizard'
      elif number== 4:
        return 'Scissors'
      else: "Error2"
def rpsls(player_choice):
    print ''
    print 'Player chooses', player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 4)
    comp_choice = number_to_name(comp_number)
    print 'Computer chooses', comp_choice
    result = (comp_number - player_number) % 4
    if result == 1 or result == 2:
        print'Computer Win!'
    elif result == 3 or result == 4:
        print 'Player Win!'
    else:
        print 'nobody won'

        
rpsls("Rock")
rpsls("Spock")
rpsls("Paper")
rpsls("Lizard")
rpsls("Scissors")