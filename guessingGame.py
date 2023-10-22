import random
guesses = 0
guess_limit = 3

secret_num = random.randint(1, 10)
while guesses < guess_limit:
    guess = int(input("Guess a number: "))
    guesses += 1
    if guess == secret_num:
        print("You got it!")
        break
else:
    print(f"You lost! The number was {secret_num}.")
