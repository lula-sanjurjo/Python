# Book: Automate the Boring Stuff with Python
# Chapter: 3. Loops

import sys

while True:
    print('Type exit to exit.')
    response = input('>')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')