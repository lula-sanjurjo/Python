# Book: Automate the Boring Stuff with Python
# Chapter: 3. Loops

# This is a Rock, Paper, Scissors game.
import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

# Game Loop
while True:
    # Display options
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
    
    # User input loop
    while True:
        selection = input('>')
        if selection == 'q':
            print('Goodbye!')
            sys.exit()
        elif selection == 'r' or selection == 'p' or selection == 's':
            break
        else:
            print('Invalid input. Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')

    if selection == 'r':
        print('ROCK versus...')
    elif selection == 'p':
        print('PAPER versus...')
    else:
        print('SCISSORS versus...')

    # Computer choice
    computer = random.randint(1, 3)
    if computer == 1:
        computer = 'r'
        print ('ROCK!')
    elif computer == 2:
        computer = 'p'
        print ('PAPER!')
    else:
        computer = 's'
        print ('SCISSORS!')

    # Show who wins
    if selection == computer:
        print('It is a tie!')
        ties += 1
    elif (selection == 'r' and computer == 's') or (selection == 'p' and computer == 'r') or (selection == 's' and computer == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1