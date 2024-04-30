first_name = 'Ethan'
last_name = 'Fitch'

# these are different ways to tell it to print the first amd last name
#output = 'Hello, ' + first_name + ' ' + last_name
#output = 'Hello, {} {}' .format(first_name, last_name)

# this will print the first name ans last name
# but specifies the parameters, making it simple to swap them
#output = 'Hello, {1}, {0}' .format(first_name, last_name)

# This is a streamlined way to do the same task, but onlky works in Python 3
#output = f'Hello, {first_name} {last_name}'
# print(output)

# by using the {} we can specify the order that the names display
print(first_name + ' ' + last_name)
print('{1} {0}'.format(first_name, last_name))
print('{0} {1}'.format(first_name, last_name))
print('{0} {0}'.format(first_name, last_name))

# to print a format string, use print(f'{a}{b}) with a and b as the variables

print(f'{first_name} {last_name}')
# This is the most efficient way to do this, the f is for function
# there are a ton of helpful string functions to use in python 
# a list of them can be found on the w3 schools website called "Python String Methods"

# Text can easily be added 
print(f'Your name is : {first_name} {last_name}')
