"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

A = input('Enter e to encrypt, d to decrypt, or q to quit: ')

if A == 'e':
    message = input('Message: ')
    key = input('Key: ')
    a = zip(message, key)
    for m in a:
        if len(key) == len(message):
            b = associations.find(m[0])
            c = associations.find(m[1])
            print(associations.find(b+c))
        elif len(key) > len(message):
            key = key[0:len(message)]
            b = associations.find(m[0])
            c = associations.find(m[1])
            print(b+c)
        else:
            l = (len(message)/len(key))
            key = key*l
            b = associations.find(m[0])
            c = associations.find(m[1])
            print(b+c)
elif A == 'd':
    message2 = input('Message: ')
    key2 = input('Key: ')
    for j in message2:
        print(associations[j])
elif A == 'q':
    print('Goodbye!')
else:
    print('Did not understand, try again.')
