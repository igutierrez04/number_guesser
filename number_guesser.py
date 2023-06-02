import random

highest_num = input("Type a range: ")

if highest_num.isdigit():
    highest_num = int(highest_num)

    if highest_num <= 0:
        print('Please type a number greater than 0.')
        quit()
else:
    print('Please type a number.')
    quit()

random_num = random.randint(0, highest_num)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Type a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number.')
        continue
    
    if user_guess == random_num:
        print("You guessed it!")
        break
    elif user_guess > random_num:
            print("You guessed too high!")
    else:
        print("You guessed too low!")

print(f"You got in {guesses} guesses")