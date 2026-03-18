# Book: Automate the Boring Stuff with Python
# Chapter: 4. Functions

def collatz(n):
    if (n % 2 == 0):
        return (n // 2)
    else:
        return(3 * n + 1)

n = input('Enter an integer number: ')
try:
    n = int(n)
    while n != 1:
        print(n, end=' ')
        n = collatz(n)
    print(n) # One last print to show that we arrived to 1
except ValueError:
    print('Please enter a valid integer number.')
