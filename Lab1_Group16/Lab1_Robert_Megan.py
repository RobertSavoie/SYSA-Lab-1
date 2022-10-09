# Program Name: Password Generator
# Names: Robert Savoie, Megan Gagliardi
# Date: Oct 07/2022
# Description: A program that generates a random strong password based on user's instructions

import random
import string


def get_random_password(num_of_letters: int, num_of_digits: int, num_of_special: int) -> int:
    letters = string.ascii_letters
    numbers = string.digits
    characters = string.punctuation
    result = ''.join(random.choice(letters) for i in range(num_of_letters))
    result += ''.join(random.choice(numbers) for i in range(num_of_digits))
    result += ''.join(random.choice(characters) for i in range(num_of_special))
    result = ''.join(random.sample(result, len(result)))

    print(f"Your desired password is: {result}")


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
        if numOfLetters not in range(0, passLen - 1):
            print(f'The number of letters should be in the range of 0 and {passLen - 2}')
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
            print(f'The number of digits should be in the range of 0 and {charRem - 1}')

    except ValueError:
        print("Input must be a whole number")

charRem = charRem - numOfDigits
cont = True

while cont:
    try:
        numOfSpecial = int(input('Please enter the number of special characters desired in the password: '))
        if numOfSpecial in range(0, charRem + 1):
            cont = False
        else:
            print(f'The number of special characters should be in the range of 0 and {charRem}')

    except ValueError:
        print('Input must be a whole number')
       
charRem = charRem - numOfSpecial
numOfLetters = numOfLetters + charRem

get_random_password(numOfLetters, numOfDigits, numOfSpecial)
