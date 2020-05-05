
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:

    guess_count += 1
    if guess_count > guess_limit:
        print("You are failed since you have tried " + str(guess_limit) + " times.")
        out_of_guesses = True
    else:
        guess = input("Enter guess: ")

if not out_of_guesses:
    print("Congratulations! You got it. You are winner since you guess the word rightly in " + str(guess_limit) + " times. ")
else:
    print("Out of guesses! YOU LOSE.")