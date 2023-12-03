'''
Determine which games would have been possible if the bag had been 
loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?

'''

import fileinput
import re

id = 0
total = 0
    
for line in fileinput.input(files ='input2.txt'):
    id += 1
    list = line.split(":")[1].strip()
    game = re.split(";|,", list)
    impossible = False
    for set in game:
        red = 0
        green = 0
        blue = 0
        num = int(re.findall('\d+', set)[0])
        if 'red' in set:
            red += num
        elif 'green' in set:
            green += num
        elif 'blue' in set:
            blue += num
        
        if red > 12 or green > 13 or blue > 14:
            impossible = True
            break
    if not impossible:
        total += id

print(total)
    

    
