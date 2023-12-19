'''
Your calculation isn't quite right. It looks like some of the digits are actually spelled out 
with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Consider your entire calibration document. What is the sum of all of the calibration values?

'''
import fileinput
total = 0

spelled = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in fileinput.input(files ='1_trebuchet/input_aoc_day1.txt'): 
    num = []
    for i, char in enumerate(line):
        if char.isdigit():
            num.append(char)
        elif char.isalpha():
            for name in spelled:
                if name == line[i:i+len(name)]:
                    num.append(str(spelled.index(name)))
    total += int(str(num[0]) +str(num[-1]))
print(total)