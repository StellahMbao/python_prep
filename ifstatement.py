# if statements allows program to respond to input given, making programs a lot smarter
is_female = False
is_fat = False
if is_female or is_fat:
    print('You are female, fat, or both')
else:
    print('You are neither female nor fat')
if is_female and is_fat:
    print('You are a fat female')
else:
    print('You aren\'t a fat female')

# if statements and comparisons
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(15, 21, 33))

    