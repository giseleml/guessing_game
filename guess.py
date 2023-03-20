import random
star_line = "*****************************"

secret_number = round(int(random.random() * 100))
total_tries = 3

print(star_line + "\n" + "Welcome to the guessing game!" + "\n" + star_line)

for current_try in range(1, total_tries + 1):
    print("\n Try {} out of {}".format(current_try, total_tries))
    user_guess_str = input("\n Insert a number between 1 and 100:")
    user_guess = int(user_guess_str)

    if user_guess < 1 or user_guess > 100:
        print("\n Number is not valid. Choose a number between 1 and 100.")
        continue

    print("\n You guessed ", user_guess)

    if user_guess == secret_number:
        print("\n You guessed correctly!")
        break
    else:
        if secret_number > user_guess:
            print("\n Wrong guess: value is higher.")
        else:
            print("\n Wrong guess: value is lower.")

print(star_line + "\n" + "Game Over. Number was {}".format(secret_number) + "\n" + star_line)
