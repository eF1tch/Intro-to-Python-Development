#first_name = 'Ethan'
#last_name  = 'Fitch'

first_name = input('Please enter your first name:')
last_name = input('Please enter your last name:')
#print(first_name + last_name)
print('Hello, ' + first_name.capitalize() + ' ' + last_name.capitalize())
# The .capitalize only works if you add a () after, Why? Because the
# .capitalize is a function, you need to tell it to use the function

sentence = "This is a longer sentince with many words"
print(sentence)
print(f"There are {sentence.lower().count("t")} t's in the sentence")
# This is an example of using the .lower (make it lower case) 
# and .count (count the specified data) functions
