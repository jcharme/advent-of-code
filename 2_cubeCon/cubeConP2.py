'''
The power of a set of cubes is equal to the numbers of red, green, 
and blue cubes multiplied together. The power of the minimum set of 
cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, 
respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been 
present. What is the sum of the power of these sets?
'''
import fileinput
import re

id = 0
total = 0

for line in fileinput.input(files ='input2.txt'):
    red = 0
    green = 0
    blue = 0
    id += 1
    list = line.split(":")[1].strip()
    game = re.split(";|,", list)
    for set in game:
        num = int(re.findall('\d+', set)[0])
        if 'red' in set:
            if num > red:
                red = num
        elif 'green' in set:
            if num > green:
                green = num
        elif 'blue' in set:
            if num > blue:
                blue = num
    total += red * green * blue
print(total)
