'''
Your calculation isn't quite right. It looks like some of the digits are actually spelled out 
with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Consider your entire calibration document. What is the sum of all of the calibration values?

'''
import fileinput

total = 0

for line in fileinput.input(files ='input_aoc_day1.txt'): 
    num = [i  for i in line if i.isdigit()]
    total += int(str(num[0]) +str(num[-1]) )

print(total)