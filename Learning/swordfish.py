# Book: Automate the Boring Stuff with Python
# Chapter: 3. Loops

while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('>')
    if password == 'swordfish':
        break

for i in range(3, 0, -1):
    print(str(i) + '...')
print('Access granted.')