# Book: Automate the Boring Stuff with Python
# Chapter: 4. Functions

def spam(divide_by):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divide_by
    except ZeroDivisionError:
        # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

number = int(input('Enter a number: '))
print(spam(number))