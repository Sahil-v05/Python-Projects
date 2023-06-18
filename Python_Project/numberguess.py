import random

wining_number = random.randint(1,50)

num_guesses = 0

print('Welcome to the number guessing game ')
print('I am thinking a number between 1 and 100 :')

while True:
    guess = int(input("please guess your  number "))

    num_guesses += 1

    if guess < wining_number:
        print("try again too low")
    elif guess > wining_number:
        print('very close but its very high')
    else:
        print("Congrulation ! You guesses the number", num_guesses, "guesses ")

print("thanks for playing")