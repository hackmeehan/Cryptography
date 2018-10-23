"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

A = input('Enter e to encrypt, d to decrypt, or q to quit: ')

if A == 'e':
    message = input('Message: ')
    key = input('Key: ')
    z = len(message)
    f = len(key)
    a = zip(message, key)
    if f == z:
        for l in a:
            b = associations.find(l[0])
            c = associations.find(l[1])
            d = b+c
            e = str(associations[d])
            print(e, end="")
    if f < z:
        e = z/f
        import math
        r = math.ceil(e)
        key = r*key
        for l in zip(message, key):
            b = associations.find(l[0])
            c = associations.find(l[1])
            d = (b+c)
            e = associations[d]
            q = print(e, end="")
    if f > z:
        for l in a:
            b = associations.find(l[0])
            c = associations.find(l[1])
            d = (b+c)
            e = associations[d]
            print(e, end="")
            
elif A == 'd':
    message2 = input('Message: ')
    key2 = input('Key: ')
    z = len(message2)
    f = len(key2)
    a = zip(message2, key2)
    if f == z:
        for l in a:
            b = associations.find(l[0])
            c = associations.find(l[1])
            d = b-c
            e = str(associations[d])
            print(e, end="")
    if f < z:
        e = z/f
        import math
        r = math.ceil(e)
        key2 = r*key2
        for l in zip(message2, key2):
            b = associations.find(l[0])
            c = associations.find(l[1])
            d = (b-c)
            e = associations[d]
            q = print(e, end="")
    if f > z:
        for l in a:
            b = associations.find(l[0])
            c = associations.find(l[1])
            d = (b-c)
            e = associations[d]
            print(e, end="")
        
elif A == 'q':
    print('Goodbye!')
else:
    print('Did not understand, try again.')
    
# +KF;B(CH=NIZ}m;R\Dt
