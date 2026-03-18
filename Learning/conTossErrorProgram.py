# Book: Automate the Boring Stuff with Python
# Chapter: 5. Debugging

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

# The error is assigning 0 and 1 values
#toss = random.randint(0, 1)  # 0 is tails, 1 is heads
toss = random.choice(['heads', 'tails'])

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')