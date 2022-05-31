## guessing game, we have our secret word variable stored, users will be required to keep guessing until they guess correct word
secret_word = 'Mango'
user_guess = ''
while user_guess != secret_word:
    user_guess = input ('Enter another guess:')

print('Well done, you\'ve guessed the correct word!')