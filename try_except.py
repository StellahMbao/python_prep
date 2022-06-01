# try except
# try:
    # number = int(input('Enter a number:'))
    # print(number)
# except:
    # print('Invalid entry')

# open file on py, using open, and the mode can either be 'r' for read only, 'a', for appending the file, and 'r+' for read and write
open_file = open('index.css', 'r+')
# to close file, open_file.close()
print(open_file.read())

## readline, readable
print(open_file.readline())
print(open_file.readline())
open_file.close()
##
