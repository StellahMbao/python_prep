# raising one number to the power of another number
def pow_of_num (base_num, pow_number):
    result = 1
    for index in range (pow_number):
        result = result * base_num
    return result
print (pow_of_num(5,4))

# 2D nested lists- list within a list
random_number = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#access an element from list, define row and column index
print(random_number[1] [0])



