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
            print(e)
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
            q = print(e)
    if f > z:
        for l in a:
            b = associations.find(l[0])
            c = associations.find(l[1])
            d = (b+c)
            e = associations[d]
            print(e)
            
elif A == 'd':
    message2 = input('Message: ')
    key2 = input('Key: ')
    '''for o in message2:
        p = associations.find(o)
    for u in key2:
        t = associations.find(u)
        print(associations[p-t])'''
    for q in message2:
        for s in key2:
            B = associations.find(q[0])
            C = associations.find(s[0])
            D = (B-C)
            E = associations[D]
            print(E)
elif A == 'q':
    print('Goodbye!')
else:
    print('Did not understand, try again.')
    
# +KF;B(CH=NIZ}m;R\Dt
