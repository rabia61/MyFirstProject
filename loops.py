secret_number = 9
max_number_of_guesses = 3
trial_number = 0

while trial_number < max_number_of_guesses:
    trial_number += 1
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You Won")
        break
else:
    print("You lost")