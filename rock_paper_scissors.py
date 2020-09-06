"""
Rock paper scissors
"""
import random
import simplegui

COMPUTER_SCORE = 0
HUMAN_SCORE = 0
TIE = 0
human_choice = ''
computer_choice = ''


def choice_to_number(choice):
    return {'rock':0,'paper':1,'scissors':2}[choice]


def number_to_choice(number):
   
    return {0:'rock',1:'paper',2:'scissors'}[number]


def random_computer_choice():
    choice = ['rock' ,'sessiors', 'paper']
    return random.choice(choice)

def choice_result(human_choice, computer_choice):
    global COMPUTER_SCORE
    global HUMAN_SCORE
    global TIE
 

    if (human_choice == 'paper' and computer_choice =='paper') or (human_choice == 'rock' and computer_choice =='rock') or (human_choice == 'scissors' and computer_choice =='scissors'): 
        print('Tie')
        TIE = TIE + 1
        return TIE
    if human_choice == 'rock' and computer_choice == 'paper':
        print('Computer Wins!!!')
        COMPUTER_SCORE = COMPUTER_SCORE + 1
        return COMPUTER_SCORE
    
    if human_choice == 'rock' and computer_choice == 'scissors':
        print('Human Wins!!!')
        HUMAN_SCORE = HUMAN_SCORE + 1
        return HUMAN_SCORE
    
    if human_choice == 'scissors' and computer_choice == 'rock':
        print('Computer Wins!!!')
        COMPUTER_SCORE = COMPUTER_SCORE + 1
        return COMPUTER_SCORE
    
    if human_choice == 'paper' and computer_choice == 'rock':
        print('Human Wins!!!')
        HUMAN_SCORE = HUMAN_SCORE + 1
        return HUMAN_SCORE
    
    if human_choice == 'scissors' and computer_choice == 'paper':
        print('Human Wins!!!')
        HUMAN_SCORE = HUMAN_SCORE + 1
        return HUMAN_SCORE
    
    if human_choice == 'paper' and computer_choice == 'scissors':
        print('Computer Wins!!!')
        COMPUTER_SCORE = COMPUTER_SCORE + 1
        return COMPUTER_SCORE
    
    

    

# This will test the code.
def test_choice_to_number():
    assert choice_to_number('rock') == 0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2
    
def test_number_to_choice():
    assert number_to_choice(0) == 'rock'
    assert number_to_choice(1) == 'paper'
    assert number_to_choice(2) == 'scissors'
    
def test_all():
    test_choice_to_number()
    test_number_to_choice()


test_all()


# Handler for mouse click on rock button.
# This code is for the GUI part of the game.
def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
# Handler for mouse click on paper button.
def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

# Handler to draw on canvas
def draw(canvas):
    
    try:
        # Draw choices
        canvas.draw_text('You Pick :' + human_choice, [10,40], 30, 'Blue')
        canvas.draw_text('Computer Pick :' + computer_choice, [10,80], 30, 'White')
        
        # Draw scores
        canvas.draw_text('Human Score :' + str(HUMAN_SCORE), [10,150], 30, 'blue')
        canvas.draw_text('Comp Score :' + str(COMPUTER_SCORE), [10,190], 30, 'White')
        canvas.draw_text('Tie :'+ str(TIE), [10,230], 30, 'Red')
        
    except TypeError:
        pass
    

# Create a frame and assign callbacks to event handlers
def play_rps():
    frame = simplegui.create_frame('Home', 400, 300)
    frame.add_button('Rock', rock)
    frame.add_button('Paper', paper)
    frame.add_button('Scissors', scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()
 
play_rps()
