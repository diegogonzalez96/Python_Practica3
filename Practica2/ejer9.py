# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 50)
print('Well, ' + myName + ', I am thinking of a number between 1 and 50.')
encontre = False
cont = 0
while not encontre:
    print('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        encontre = True
    cont += 1
    if cont == 3:
        if number % 2 == 0:
            print("El numero es par")
        else:
            print("el numero es impar")
cont = str(cont)
if guess == number:
    print('Good job, ' + myName + '! You guessed my number in ' +
    cont + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')