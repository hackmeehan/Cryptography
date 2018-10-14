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
    for i in message:
        print(associations.find(i))
elif A == 'd':
    message2 = input('Message: ')
    for j in message2:
        print(associations[j])
elif A != ['e', 'd', 'q']:
    print('Did not understand, try again.')
elif A == 'q':
    print('Goodbye!')