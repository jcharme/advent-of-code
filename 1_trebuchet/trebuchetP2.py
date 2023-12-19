'''
Your calculation isn't quite right. It looks like some of the digits are actually spelled out 
with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Consider your entire calibration document. What is the sum of all of the calibration values?

'''
import fileinput
import re

makeNum = {
    'one' : 1,
    'two' : 2,
    'three': 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}

total = 0

for line in fileinput.input(files ='input1.txt'): 
    num = [i for i in line if i.isdigit() else makeNum]
    total += int(str(num[0]) +str(num[-1]) )

print(total)