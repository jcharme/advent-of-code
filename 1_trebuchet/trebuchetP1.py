'''
The newly-improved calibration document consists of lines of text; each line originally 
contained a specific calibration value that the Elves now need to recover. On each line, 
the calibration value can be found by combining the first digit and the last digit (in 
that order) to form a single two-digit number.

Consider your entire calibration document. What is the sum of all of the calibration values?

'''
import fileinput

total = 0

for line in fileinput.input(files = '/home/jcharme/repos/aoc23/1_trebuchet/input1.txt'): 
    num = [i for i in line if i.isdigit()]
    total += int(str(num[0]) +str(num[-1]) )

print(total)