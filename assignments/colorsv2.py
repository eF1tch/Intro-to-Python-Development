favorite_color = input ('What is your favorite color?')
print('Oh, your favorite color is',favorite_color,'?')
answer = input ('really? (yes or no)')
if answer == 'yes': print(favorite_color,'is my favorite color too! :)')
else:
    if answer == 'no' : print('Why would you lie to me? :(')
    else: print('It is a yes or no question "',answer,'" is not a valid answer. Apologies if that was too complex for you.')