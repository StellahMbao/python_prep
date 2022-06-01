def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower in ('aieou'):
            translation = translation + 'g'
        if letter.isupper in ('aeiou'):
            translation = translation + 'G'
        else:
            translation = translation + letter
    return translation
# print(translate(input('Enter a phrase:')))
'''
writing comments using tripple quotations
'''