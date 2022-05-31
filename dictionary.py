# dictionary allows us to store information in key value pairs
#dictonary words enclosed in curly brackets

month_dictionary = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

## Access word from dictionary, method 1
print(month_dictionary["Sep"])

#method2
print(month_dictionary.get('Dec'))

#for a key that is not on the list
print(month_dictionary.get('ok', 'Not a valid key'))





## while loop- block of code executed multiple times
age = 1
while age <= 10:
    print(age)
    age += 1
print('Done with loop')