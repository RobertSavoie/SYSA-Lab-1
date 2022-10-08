# Program Name: Password Generator
# Names: Robert Savoie, Megan Gagliardi
# Date: Oct 07/2022
# Description: A program that generates a random strong password based on user's instructions

import random
import string

cont = True
passLen = 0
numOfLetters = 0
numOfDigits = 0
numOfSpecial = 0

while cont:
    try:
        passLen = int(input("Please enter the length of the password: "))
        if passLen < 8:
            print('Please enter a value of greater than or equal to 8 to create a secure password')
        else:
            cont = False

    except ValueError:
        print("Input must be a whole number")

cont = True

while cont:
    try:
        numOfLetters = int(input('Please enter the number of letters desired in the password: '))
        if numOfLetters not in range(0, passLen-1):
            print(f'The number of letters should be in the range of 0 and {passLen-2}')
        else:
            cont = False

    except ValueError:
        print("Input must be a whole number")

charRem = passLen - numOfLetters
cont = True

while cont:
    try:
        numOfDigits = int(input('Please enter the number of digits desired in the password: '))
        if numOfDigits in range(0, charRem):
            cont = False
        else:
            print(f'The number of digits should be in the range of 0 and {charRem-1}')

    except ValueError:
        print("Input must be a whole number")

charRem = charRem - numOfDigits
cont = True

while cont:
    try:
        numOfSpecial = int(input('Please enter the number of special characters desired in the password: '))
        if numOfSpecial in range(0, charRem+1):
            cont = False
        else:
            print(f'The number of special characters should be in the range of 0 and {charRem}')

    except ValueError:
        print('Input must be a whole number')

print(numOfLetters, numOfDigits, numOfSpecial)

# def get_random_password():
#     random_source = string.ascii_letters + string.digits + string.punctuation
#     password = random.choice(numOfLetters)
#     password += random.choice(numOfDigits)
#     password += random.choice(numOfSpecial)
#
#     for i in range(passLen):
#         password += random.choice(random_source)
#
#     password_list = list(password)
#
#     random.SystemRandom().shuffle(password_list)
#     password = ''.join(password_list)
#     return password
#
#
# print('Your desired password is: ', get_random_password())

