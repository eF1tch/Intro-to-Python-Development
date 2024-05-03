import random
print('\nPlease enter the following:\n')
adj = input('adjective: ')
animal = input('animal: ')
verb0 = input('gerund (-ing verb): ')
yell = input('exclamation: ')
verb1 = input('action verb: ')
verb2 = input('verb: ')

# Lines 12 - 17 are fillers for faster testing (comment out rows 2 to 8)

# adj = 'drunk'
# animal = 'hippo'
# verb0 = 'waltzing'
# yell = "oh great heavens"
# verb1 = 'roll'
# verb2 = 'twerk'

libpicker = [1,2]
variable = random.choice(libpicker)

# These were used to test individual outputs (comment out rows 17 to 18)
# variable = 1
# variable = 2

if variable == 1: print(f'\nYour story is:\n\nThe other day, I was really in trouble. It all started when I saw a very \n{adj.lower()} {animal.lower()} {verb0.lower()} down the hallway. "{yell.capitalize()}" I yelled. But all \nI could think to do was to {verb1.lower()} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb2.lower()} \nright in front of my family.\n')
if variable == 2: print(f'\nYour story is:\n\nIn the {adj.lower()} meadow, a {animal.lower()} was {verb0.lower()} in the swaying grass. \n"{yell.capitalize()}" I exclaimed. My heart brimming with anticipation, \nI began to {verb1.lower()} towards the {animal.lower()}, and admired the {animal.lower()} {verb0.lower()} with elegance. \nAs a way to show my respect, I decided to {verb2.lower()} beside it, \ncherishing this moment of tranquility in nature.')