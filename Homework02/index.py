import simplegui 
import random
import math
num_range = 100
secret = 0
user_guess = 0
num_guesses = 7
def new_game():
    global secret_number
    global number_of_guesses
    secret_number = random.randrange(0 , 101)
  
    number_of_guesses = 7
    print""
    print "New Game!! Curren range set to 0-100"
    
    
def range100():
    global secret_number
    global number_of_guesses
    secret_number = random.randrange(0 , 101)
    number_of_guesses = 7
   
    print"New Game!! Curren range set to 0-100"
def range1000():
    global secret_number
    global number_of_guesses
    secret_number = random.randrange(0, 1001)
    number_of_guesses = 10
  
    print"New Game!! Current range set to 0-1000"
def input_guess(guess):
    global number_of_guesses
    guess = int(guess)
    print""
    print "Guess was:",guess
    print""
    if guess > secret_number and number_of_guesses > 0:
        print"Lower"
        print""
        number_of_guesses -= 1
        print "Guesses remaining:", number_of_guesses
        print""
      
    elif guess < secret_number and number_of_guesses > 0:
        print"Higher!"
        print""
        number_of_guesses -= 1
        print "Guesses Remaining: ", number_of_guesses
        
    elif number_of_guesses > 0 and guess == secret_number:
        print "You Win!!!"
        new_game()
    elif number_of_guesses <= 1:
        print "Game Over! Out Of Guesses!"
        new_game()

    else:
        print"Something wrong"
        new_game()
    
    
frame = simplegui.create_frame("Guess The Number", 200 , 200)

frame.add_button('Range [0 , 100]',range100, 200)
frame.add_button('Range [0 , 1000]', range1000, 200)
frame.add_input('Enter guess', input_guess, 50)
new_game()
frame.start()
