star_line = "*****************************"
print(star_line)
print("Welcome to the guessing game!")
print(star_line)

secret_number = 77
total_tries = 3
current_try = 1

while current_try <= total_tries:
    print("\n Try {} out of {}".format(current_try, total_tries))
    user_guess_str = input("\n Insert a number:")
    user_guess = int(user_guess_str)

    print("\n You guessed ", user_guess)

    if user_guess == secret_number:
        print("\n You guessed correctly!")
        current_try = total_tries
    else:
        if user_guess > secret_number:
            print("\n Wrong guess: value is higher.")
        else:
            print("\n Wrong guess: value is lower.")

    current_try = current_try + 1

print(star_line)
print("Game Over.")
print(star_line)
