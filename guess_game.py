## guessing game, we have our secret word variable stored, users will be required to keep guessing until they guess correct word
secret_word = 'Mango'
user_guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False
while user_guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        user_guess = input ('Enter guess:')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, You lose")
else:
    print("You win! Congratulations!")
